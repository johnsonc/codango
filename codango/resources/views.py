import json
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View, TemplateView
from django.db.models import Count
from resources.models import Resource
from comments.forms import CommentForm
from resources.forms import ResourceForm
from votes.models import Vote
from django.core.urlresolvers import reverse


class CommunityBaseView(TemplateView):
    template_name = 'account/home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            self.template_name = 'account/partials/community.html'
        return super(CommunityBaseView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        sortby = self.request.GET[
            'sortby'] if 'sortby' in self.request.GET else 'date'

        resources = self.sort_by(sortby, Resource.objects)
        community = kwargs[
            'community'].upper() if 'community' in kwargs else 'ALL'

        if community != 'ALL':
            resources = resources.filter(language_tags=community)
        context = {
            'resources': resources,
            'commentform': CommentForm(auto_id=False),
            'title': 'Activity Feed',
            'popular': Resource.objects.annotate(num_comments=Count('comments')).annotate(num_votes=Count('votes')).order_by('-num_comments', '-num_votes')[:5],
        }
        return context

    @staticmethod
    def sort_by(sorting_name, object_set):
        if sorting_name == 'date':
            return object_set.order_by('-date_modified')
        else:
            return object_set.annotate(num_sort=Count(sorting_name)).order_by('-num_sort')


class CommunityView(CommunityBaseView):
    form_class = ResourceForm

    def post(self, request, *args, **kwargs):

        try:
            form = self.form_class(request.POST, request.FILES)
            resource = form.save(commit=False)
            try:
                resource.resource_file_name = form.files['resource_file'].name
                resource.resource_file_size = form.files['resource_file'].size
            except KeyError:
                pass
            resource.author = self.request.user
            resource.save()
            return HttpResponse("success", content_type='text/plain')
        except ValueError:
            return HttpResponseNotFound("emptypost")
        except:
            return HttpResponseNotFound("invalidfile")


class ResourceVoteView(View):

    def post(self, request, **kwargs):
        action = kwargs['action']
        resource_id = kwargs['resource_id']
        resource = Resource.objects.filter(id=resource_id).first()
        user_id = self.request.user.id
        vote = Vote.objects.filter(
            resource_id=resource_id, user_id=user_id).first()
        vote_mapping = {
            'like': True,
            'unlike': False,
        }
        # Create a vote object if the user has not voted yet
        if vote is None:
            vote = Vote()
            vote.resource = resource
            vote.user = self.request.user
        if vote.vote is None or vote.vote is not vote_mapping[action]:
            # If user has not voted yet or is changing his vote set vote to
            # current vote
            vote.vote = vote_mapping[action]
            status = action
            vote.save()
        else:
            vote.delete()
            status = "unvotes"

        response_dict = {
            "upvotes": len(resource.upvotes()),
            "downvotes": len(resource.downvotes()),
            "status": status,
            "content": vote.user.username+ " " + status  + " your resource",
            "link": "http://codango-stanging/resource/1",
            "type": "vote",
            "read": False,
            "user_id": resource.author.id
            }

        response_json = json.dumps(response_dict)
        return HttpResponse(response_json, content_type="application/json")
