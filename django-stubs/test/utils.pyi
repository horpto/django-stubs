from io import StringIO
from collections import OrderedDict
from contextlib import _GeneratorContextManager
from decimal import Decimal
from django.apps.registry import Apps
from django.conf import LazySettings
from django.db import DefaultConnectionProxy
from django.db.backends.dummy.base import DatabaseWrapper
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.template.base import Template
from django.template.context import Context
from django.test.runner import DiscoverRunner
from django.test.testcases import SimpleTestCase
from django.utils.safestring import SafeText
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)


def captured_output(stream_name: str) -> Iterator[StringIO]: ...


def captured_stderr() -> _GeneratorContextManager: ...


def captured_stdout() -> _GeneratorContextManager: ...


def compare_xml(want: str, got: str) -> bool: ...


def dependency_ordered(
    test_databases: List[Tuple[str, Tuple[str, List[str]]]],
    dependencies: Dict[str, List[str]]
) -> List[Tuple[str, Tuple[str, List[str]]]]: ...


def extend_sys_path(*paths) -> Iterator[None]: ...


def freeze_time(t: int) -> Iterator[None]: ...


def get_runner(
    settings: LazySettings,
    test_runner_class: Optional[str] = ...
) -> Type[DiscoverRunner]: ...


def get_unique_databases_and_mirrors() -> Tuple[OrderedDict, Dict[Any, Any]]: ...


def instrumented_test_render(
    self: Template,
    context: Context
) -> SafeText: ...


def require_jinja2(test_func: Callable) -> Callable: ...


def setup_databases(
    verbosity: int,
    interactive: bool,
    keepdb: bool = ...,
    debug_sql: bool = ...,
    parallel: int = ...,
    **kwargs
) -> Union[List[Tuple[DatabaseWrapper, str, bool]], List[Tuple[DatabaseWrapper, str, bool]]]: ...


def setup_test_environment(debug: bool = ...) -> None: ...


def tag(*tags) -> Callable: ...


def teardown_databases(
    old_config: List[Tuple[DatabaseWrapper, str, bool]],
    verbosity: int,
    parallel: int = ...,
    keepdb: bool = ...
) -> None: ...


def teardown_test_environment() -> None: ...


class Approximate:
    def __eq__(self, other: Union[float, Decimal]) -> bool: ...
    def __init__(self, val: Union[float, Decimal], places: int = ...) -> None: ...


class CaptureQueriesContext:
    def __enter__(self) -> CaptureQueriesContext: ...
    def __exit__(self, exc_type: None, exc_value: None, traceback: None) -> None: ...
    def __getitem__(self, index: int) -> Dict[str, str]: ...
    def __init__(
        self,
        connection: Union[DefaultConnectionProxy, backends.sqlite3.base.DatabaseWrapper]
    ) -> None: ...
    def __len__(self) -> int: ...
    @property
    def captured_queries(self) -> List[Dict[str, str]]: ...


class ContextList:
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: Union[str, int]) -> Any: ...
    def get(self, key: str, default: None = ...) -> str: ...


class LoggingCaptureMixin:
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...


class TestContextDecorator:
    def __call__(self, decorated: Any) -> Any: ...
    def __enter__(self) -> Optional[Apps]: ...
    def __exit__(self, exc_type: None, exc_value: None, traceback: None) -> None: ...
    def __init__(self, attr_name: Optional[str] = ..., kwarg_name: Optional[str] = ...) -> None: ...
    def decorate_callable(self, func: Callable) -> Callable: ...
    def decorate_class(
        self,
        cls: Type[SimpleTestCase]
    ) -> Type[SimpleTestCase]: ...


class ignore_warnings:
    def __init__(self, **kwargs) -> None: ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...


class isolate_apps:
    def __init__(self, *installed_apps, **kwargs) -> None: ...
    def disable(self) -> None: ...
    def enable(self) -> Apps: ...


class modify_settings:
    def __init__(self, *args, **kwargs) -> None: ...
    def enable(self) -> None: ...
    def save_options(self, test_func: Type[SimpleTestCase]) -> None: ...


class override_script_prefix:
    def __init__(self, prefix: str) -> None: ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...


class override_settings:
    def __init__(self, **kwargs) -> None: ...
    def decorate_class(
        self,
        cls: Type[Union[SimpleTestCase, LoggingCaptureMixin]]
    ) -> Type[Union[SimpleTestCase, LoggingCaptureMixin]]: ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...
    def save_options(
        self,
        test_func: Type[Union[SimpleTestCase, LoggingCaptureMixin]]
    ) -> None: ...


class override_system_checks:
    def __init__(self, new_checks: List[Callable], deployment_checks: Optional[List[Callable]] = ...) -> None: ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...