from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


def retrieve_user(request) -> User:
    session_id = request.COOKIES.get("sessionid")
    session = Session.objects.get(session_key=session_id)
    uid = session.get_decoded().get("_auth_user_id")
    user = User.objects.get(pk=uid)

    return user
