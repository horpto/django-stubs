from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls.resolvers import URLPattern
from typing import (
    Dict,
    List,
    Tuple,
    Union,
)


class GroupAdmin:
    def formfield_for_manytomany(
        self,
        db_field: ManyToManyField,
        request: WSGIRequest = ...,
        **kwargs
    ) -> ModelMultipleChoiceField: ...


class UserAdmin:
    def _add_view(
        self,
        request: WSGIRequest,
        form_url: str = ...,
        extra_context: None = ...
    ) -> Union[TemplateResponse, HttpResponseRedirect]: ...
    def add_view(
        self,
        request: WSGIRequest,
        form_url: str = ...,
        extra_context: None = ...
    ): ...
    def get_fieldsets(
        self,
        request: WSGIRequest,
        obj: None = ...
    ) -> Tuple[Tuple[None, Dict[str, Union[Tuple[str], Tuple[str, str, str]]]]]: ...
    def get_urls(self) -> List[URLPattern]: ...
    def lookup_allowed(self, lookup: str, value: str) -> bool: ...
    def response_add(
        self,
        request: WSGIRequest,
        obj: User,
        post_url_continue: None = ...
    ) -> HttpResponseRedirect: ...
    def user_change_password(
        self,
        request: WSGIRequest,
        id: str,
        form_url: str = ...
    ) -> Union[TemplateResponse, HttpResponseRedirect]: ...