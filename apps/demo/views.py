from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment

# Create a custom pagination class for the posts
class PostPagination(PageNumberPagination):
    page_size = 3  # You can adjust this to control how many posts per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostListView(APIView):

    def get(self, request, *args, **kwargs):
        # Fetch all posts ordered by timestamp, latest first
        posts = Post.objects.all().order_by('-timestamp')

        # Paginate the posts using the custom PostPagination
        paginator = PostPagination()
        result_page = paginator.paginate_queryset(posts, request)

        # Prepare the response data
        posts_data = []
        for post in result_page:
            # Get the latest 3 comments for each post, ordered by timestamp
            comments = Comment.objects.filter(post=post).order_by('-timestamp')[:3]
            

            #comments = Comment.objects.filter(post=post).order_by('?')[:3]
            # for random 3 comments



            # Prepare post data manually
            post_data = {
                'id': post.id,
                'text': post.text,
                'timestamp': post.timestamp,
                'comment_count': post.comments.count(),
                'author_username': post.user.username,
                'comments': [
                    {
                        'text': comment.text,
                        'timestamp': comment.timestamp,
                        'author_username': comment.user.username
                    }
                    for comment in comments
                ]
            }

            posts_data.append(post_data)

        # Return paginated response
        return paginator.get_paginated_response(posts_data)
