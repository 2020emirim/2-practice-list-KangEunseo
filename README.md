# Practice_List
## bookmark
- github 소스 -> PyCharm 프로젝트
- bookmark 앱 만들기
- models Bookmark 만들기
- admin Bookmark 등록하기
- python manage.py makemigrations bookmark
- python manage.py migrate
- python manage.py createsuperuser
- models Bookmark __str__() 출력하는 문구 설정
- urls bookmark:list
- views BookmarkList
- templates bookmark_list.html
- views BookmarkCreateView
- templates bookmark_create.html
- urls add
- modify bookmark_list Add Bookmark link
- views BookmarkDetailView
- templates bookmark_detail.html
- urls detail/<int:pk>/
- modify bookmark_list detail link
- update: views BookmarkUpdateView, templates bookmark_update.html, urls, modify Modify link
- delete: views BookmarkUpdateView, templates bookmark_confirm.html, urls, modify Delete link
- pagination views, base.html, bookmark_list.html