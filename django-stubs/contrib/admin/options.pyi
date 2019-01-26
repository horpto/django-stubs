from collections import OrderedDict
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type, Union

from django.contrib.admin.filters import SimpleListFilter
from django.contrib.admin.models import LogEntry
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.contenttypes.models import ContentType
from django.core.checks.messages import Error
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.db.models.base import Model
from django.forms.fields import TypedChoiceField

from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey, ManyToManyField, RelatedField
from django.db.models.query import QuerySet
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField
from django.forms.widgets import Media
from django.http.response import HttpResponse, HttpResponseBase, HttpResponseRedirect, JsonResponse
from django.urls.resolvers import URLPattern
from django.utils.safestring import SafeText

from django.db.models.options import Options

IS_POPUP_VAR: str
TO_FIELD_VAR: str
HORIZONTAL: Any
VERTICAL: Any

def get_content_type_for_model(obj: Union[Type[Model], Model]) -> ContentType: ...
def get_ul_class(radio_style: int) -> str: ...

class IncorrectLookupParameters(Exception): ...

FORMFIELD_FOR_DBFIELD_DEFAULTS: Any
csrf_protect_m: Any

class BaseModelAdmin:
    autocomplete_fields: Any = ...
    raw_id_fields: Any = ...
    fields: Any = ...
    exclude: Any = ...
    fieldsets: Any = ...
    form: Any = ...
    filter_vertical: Any = ...
    filter_horizontal: Any = ...
    radio_fields: Any = ...
    prepopulated_fields: Any = ...
    formfield_overrides: Any = ...
    readonly_fields: Any = ...
    ordering: Any = ...
    sortable_by: Any = ...
    view_on_site: bool = ...
    show_full_result_count: bool = ...
    checks_class: Any = ...
    def check(self, **kwargs: Any) -> List[Error]: ...
    def __init__(self) -> None: ...
    def formfield_for_dbfield(self, db_field: Field, request: WSGIRequest, **kwargs: Any) -> Optional[Field]: ...
    def formfield_for_choice_field(self, db_field: Field, request: WSGIRequest, **kwargs: Any) -> TypedChoiceField: ...
    def get_field_queryset(self, db: None, db_field: RelatedField, request: WSGIRequest) -> Optional[QuerySet]: ...
    def formfield_for_foreignkey(
        self, db_field: ForeignKey, request: WSGIRequest, **kwargs: Any
    ) -> Optional[ModelChoiceField]: ...
    def formfield_for_manytomany(
        self, db_field: ManyToManyField, request: WSGIRequest, **kwargs: Any
    ) -> ModelMultipleChoiceField: ...
    def get_autocomplete_fields(self, request: WSGIRequest) -> Tuple: ...
    def get_view_on_site_url(self, obj: Optional[Model] = ...) -> Optional[str]: ...
    def get_empty_value_display(self) -> SafeText: ...
    def get_exclude(self, request: WSGIRequest, obj: Optional[Model] = ...) -> None: ...
    def get_fields(
        self, request: WSGIRequest, obj: Optional[Model] = ...
    ) -> Union[List[Union[Callable, str]], Tuple[str, str]]: ...
    def get_fieldsets(
        self, request: WSGIRequest, obj: Optional[Model] = ...
    ) -> Union[
        List[Tuple[None, Dict[str, List[Union[Callable, str]]]]],
        Tuple[Tuple[Optional[str], Dict[str, Tuple[Union[Tuple[str, str], str]]]]],
    ]: ...
    def get_ordering(self, request: WSGIRequest) -> Union[List[str], Tuple]: ...
    def get_readonly_fields(self, request: WSGIRequest, obj: Optional[Model] = ...) -> Union[List[str], Tuple]: ...
    def get_prepopulated_fields(self, request: WSGIRequest, obj: Optional[Model] = ...) -> Dict[str, Tuple[str]]: ...
    def get_queryset(self, request: WSGIRequest) -> QuerySet: ...
    def get_sortable_by(self, request: WSGIRequest) -> Union[List[Callable], List[str], Tuple]: ...
    def lookup_allowed(self, lookup: str, value: str) -> bool: ...
    def to_field_allowed(self, request: WSGIRequest, to_field: str) -> bool: ...
    def has_add_permission(self, request: WSGIRequest) -> bool: ...
    def has_change_permission(self, request: WSGIRequest, obj: Optional[Model] = ...) -> bool: ...
    def has_delete_permission(self, request: WSGIRequest, obj: Optional[Model] = ...) -> bool: ...
    def has_view_permission(self, request: WSGIRequest, obj: Optional[Model] = ...) -> bool: ...
    def has_module_permission(self, request: WSGIRequest) -> bool: ...

class ModelAdmin(BaseModelAdmin):
    formfield_overrides: Any
    list_display: Any = ...
    list_display_links: Any = ...
    list_filter: Any = ...
    list_select_related: bool = ...
    list_per_page: int = ...
    list_max_show_all: int = ...
    list_editable: Any = ...
    search_fields: Any = ...
    date_hierarchy: Any = ...
    save_as: bool = ...
    save_as_continue: bool = ...
    save_on_top: bool = ...
    paginator: Any = ...
    preserve_filters: bool = ...
    inlines: Any = ...
    add_form_template: Any = ...
    change_form_template: Any = ...
    change_list_template: Any = ...
    delete_confirmation_template: Any = ...
    delete_selected_confirmation_template: Any = ...
    object_history_template: Any = ...
    popup_response_template: Any = ...
    actions: Any = ...
    action_form: Any = ...
    actions_on_top: bool = ...
    actions_on_bottom: bool = ...
    actions_selection_counter: bool = ...
    checks_class: Any = ...
    model: Type[Model] = ...
    opts: Options = ...
    admin_site: AdminSite = ...
    def __init__(self, model: Type[Model], admin_site: Optional[AdminSite]) -> None: ...
    def get_inline_instances(self, request: WSGIRequest, obj: Optional[Model] = ...) -> List[InlineModelAdmin]: ...
    def get_urls(self) -> List[URLPattern]: ...
    @property
    def urls(self) -> List[URLPattern]: ...
    @property
    def media(self) -> Media: ...
    def get_model_perms(self, request: WSGIRequest) -> Dict[str, bool]: ...
    def get_form(self, request: Any, obj: Optional[Any] = ..., change: bool = ..., **kwargs: Any): ...
    def get_changelist(self, request: WSGIRequest, **kwargs: Any) -> Type[ChangeList]: ...
    def get_changelist_instance(self, request: WSGIRequest) -> ChangeList: ...
    def get_object(self, request: WSGIRequest, object_id: str, from_field: None = ...) -> Optional[Model]: ...
    def get_changelist_form(self, request: Any, **kwargs: Any): ...
    def get_changelist_formset(self, request: Any, **kwargs: Any): ...
    def get_formsets_with_inlines(self, request: WSGIRequest, obj: Optional[Model] = ...) -> None: ...
    def get_paginator(
        self,
        request: WSGIRequest,
        queryset: QuerySet,
        per_page: int,
        orphans: int = ...,
        allow_empty_first_page: bool = ...,
    ) -> Paginator: ...
    def log_addition(
        self,
        request: WSGIRequest,
        object: Model,
        message: Union[Dict[str, Dict[Any, Any]], List[Dict[str, Dict[str, str]]]],
    ) -> LogEntry: ...
    def log_change(
        self,
        request: WSGIRequest,
        object: Model,
        message: Union[Dict[str, Dict[str, List[str]]], List[Dict[str, Dict[str, Union[List[str], str]]]]],
    ) -> LogEntry: ...
    def log_deletion(self, request: WSGIRequest, object: Model, object_repr: str) -> LogEntry: ...
    def action_checkbox(self, obj: Model) -> SafeText: ...
    def get_actions(self, request: WSGIRequest) -> OrderedDict: ...
    def get_action_choices(
        self, request: WSGIRequest, default_choices: List[Tuple[str, str]] = ...
    ) -> List[Tuple[str, str]]: ...
    def get_action(self, action: Union[Callable, str]) -> Tuple[Callable, str, str]: ...
    def get_list_display(self, request: WSGIRequest) -> Union[List[Callable], List[str], Tuple[str]]: ...
    def get_list_display_links(
        self, request: WSGIRequest, list_display: Union[List[Callable], List[str], Tuple[str]]
    ) -> Optional[Union[List[Callable], List[str], Tuple[str]]]: ...
    def get_list_filter(self, request: WSGIRequest) -> Union[List[Type[SimpleListFilter]], List[str], Tuple]: ...
    def get_list_select_related(self, request: WSGIRequest) -> Union[Tuple, bool]: ...
    def get_search_fields(self, request: WSGIRequest) -> Union[List[str], Tuple]: ...
    def get_search_results(
        self, request: WSGIRequest, queryset: QuerySet, search_term: str
    ) -> Tuple[QuerySet, bool]: ...
    def get_preserved_filters(self, request: WSGIRequest) -> str: ...
    def construct_change_message(
        self, request: WSGIRequest, form: AdminPasswordChangeForm, formsets: None, add: bool = ...
    ) -> List[Dict[str, Dict[str, List[str]]]]: ...
    def message_user(
        self,
        request: WSGIRequest,
        message: str,
        level: Union[int, str] = ...,
        extra_tags: str = ...,
        fail_silently: bool = ...,
    ) -> None: ...
    def save_form(self, request: Any, form: Any, change: Any): ...
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None: ...
    def delete_model(self, request: WSGIRequest, obj: Model) -> None: ...
    def delete_queryset(self, request: WSGIRequest, queryset: QuerySet) -> None: ...
    def save_formset(self, request: Any, form: Any, formset: Any, change: Any) -> None: ...
    def save_related(self, request: Any, form: Any, formsets: Any, change: Any) -> None: ...
    def render_change_form(
        self,
        request: Any,
        context: Any,
        add: bool = ...,
        change: bool = ...,
        form_url: str = ...,
        obj: Optional[Any] = ...,
    ): ...
    def response_add(self, request: WSGIRequest, obj: Model, post_url_continue: Optional[str] = ...) -> HttpResponse: ...
    def response_change(self, request: WSGIRequest, obj: Model) -> HttpResponse: ...
    def response_post_save_add(self, request: WSGIRequest, obj: Model) -> HttpResponseRedirect: ...
    def response_post_save_change(self, request: WSGIRequest, obj: Model) -> HttpResponseRedirect: ...
    def response_action(self, request: WSGIRequest, queryset: QuerySet) -> Optional[HttpResponseBase]: ...
    def response_delete(self, request: WSGIRequest, obj_display: str, obj_id: int) -> HttpResponse: ...
    def render_delete_form(self, request: Any, context: Any): ...
    def get_inline_formsets(
        self, request: WSGIRequest, formsets: List[Any], inline_instances: List[Any], obj: Optional[Model] = ...
    ) -> List[Any]: ...
    def get_changeform_initial_data(self, request: WSGIRequest) -> Dict[str, str]: ...
    def changeform_view(
        self,
        request: WSGIRequest,
        object_id: Optional[str] = ...,
        form_url: str = ...,
        extra_context: Optional[Dict[str, bool]] = ...,
    ) -> Any: ...
    def autocomplete_view(self, request: WSGIRequest) -> JsonResponse: ...
    def add_view(self, request: WSGIRequest, form_url: str = ..., extra_context: None = ...) -> HttpResponse: ...
    def change_view(
        self, request: WSGIRequest, object_id: str, form_url: str = ..., extra_context: Optional[Dict[str, bool]] = ...
    ) -> HttpResponse: ...
    def changelist_view(
        self, request: WSGIRequest, extra_context: Optional[Dict[str, str]] = ...
    ) -> HttpResponseBase: ...
    def get_deleted_objects(
        self, objs: QuerySet, request: WSGIRequest
    ) -> Tuple[List[Any], Dict[Any, Any], Set[Any], List[Any]]: ...
    def delete_view(self, request: WSGIRequest, object_id: str, extra_context: None = ...) -> Any: ...
    def history_view(self, request: WSGIRequest, object_id: str, extra_context: None = ...) -> HttpResponse: ...

class InlineModelAdmin(BaseModelAdmin):
    model: Any = ...
    fk_name: Any = ...
    formset: Any = ...
    extra: int = ...
    min_num: Any = ...
    max_num: Any = ...
    template: Any = ...
    verbose_name: Any = ...
    verbose_name_plural: Any = ...
    can_delete: bool = ...
    show_change_link: bool = ...
    checks_class: Any = ...
    classes: Any = ...
    admin_site: Any = ...
    parent_model: Any = ...
    opts: Any = ...
    has_registered_model: Any = ...
    def __init__(self, parent_model: Union[Type[Model], Model], admin_site: AdminSite) -> None: ...
    @property
    def media(self) -> Media: ...
    def get_extra(self, request: WSGIRequest, obj: Optional[Model] = ..., **kwargs: Any) -> int: ...
    def get_min_num(self, request: WSGIRequest, obj: Optional[Model] = ..., **kwargs: Any) -> None: ...
    def get_max_num(self, request: WSGIRequest, obj: Optional[Model] = ..., **kwargs: Any) -> Optional[int]: ...
    fields: Any = ...
    def get_formset(self, request: Any, obj: Optional[Any] = ..., **kwargs: Any): ...
    def get_queryset(self, request: WSGIRequest) -> QuerySet: ...
    def has_change_permission(self, request: WSGIRequest, obj: Optional[Model] = ...) -> bool: ...
    def has_delete_permission(self, request: WSGIRequest, obj: Optional[Model] = ...) -> bool: ...
    def has_view_permission(self, request: WSGIRequest, obj: Optional[Model] = ...) -> bool: ...

class StackedInline(InlineModelAdmin):
    template: str = ...

class TabularInline(InlineModelAdmin):
    template: str = ...
