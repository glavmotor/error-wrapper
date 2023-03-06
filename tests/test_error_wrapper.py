from error_wrapper.error_wrapper import ErrorWrapper, ERROR_STATUS_DETAIL_PREFIX, ERROR_STATUS_NO_ERRORS, EXCEPTION_NAME_POSTFIX, run_method_if_no_errors

ARG_NUM_ERROR = 'Wrong args number: '
ARG_TYPE_ERROR = 'At least one of args has wrong type!'
REPORT_PREFIX = 'INSTANCE. '


try:
    _ = 1 / 0
except Exception as e:
    zero_division_error_text = e.__str__()


class DivNum(ErrorWrapper):

    @run_method_if_no_errors
    def test_args_number(self, *args):
        if len(args) != 2:
            self.raise_instance_error(f'{ARG_NUM_ERROR}{len(args)}')
        return

    @run_method_if_no_errors
    def test_args_type(self, *args):
        if not isinstance(args[0], int) or not isinstance(args[1], int):
            self.raise_instance_error(ARG_TYPE_ERROR)
        return

    def div(self, *args):
        self.clear_instance_error()
        self.test_args_number(*args)
        self.test_args_type(*args)
        if self.error:
            return self.error_detail
        try:
            return args[0] / args[1]
        except Exception as e:
            self.raise_instance_exception(e)
            return self.error_detail


def test_default_error_wrapper():

    obj = DivNum()
    result = obj.div(1, '2', 3)
    assert result == f'{ARG_NUM_ERROR}{3}'
    assert obj.error_detail == f'{ARG_NUM_ERROR}{3}'
    assert obj.error_status == f'{ERROR_STATUS_DETAIL_PREFIX}{ARG_NUM_ERROR}{3}'
    assert obj.exception_name is None

    result = obj.div(1, '2')
    assert result == ARG_TYPE_ERROR
    assert obj.error_detail == ARG_TYPE_ERROR
    assert obj.error_status == f'{ERROR_STATUS_DETAIL_PREFIX}{ARG_TYPE_ERROR}'
    assert obj.exception_name is None

    result = obj.div(1, 0)
    assert result == zero_division_error_text
    assert obj.error_detail == zero_division_error_text
    assert obj.error_status == f'{ERROR_STATUS_DETAIL_PREFIX}{zero_division_error_text}'
    assert obj.exception_name == ZeroDivisionError.__name__

    result = obj.div(1, 2)
    assert result == 0.5
    assert obj.error_detail is None
    assert obj.error_status == ERROR_STATUS_NO_ERRORS
    assert obj.exception_name is None


def test_error_wrapper_with_prefix():

    obj = DivNum(report_prefix=REPORT_PREFIX)
    obj.div(1, '2', 3)
    assert obj.error_detail == f'{REPORT_PREFIX}{ARG_NUM_ERROR}{3}'
    assert obj.error_status == f'{ERROR_STATUS_DETAIL_PREFIX}{REPORT_PREFIX}{ARG_NUM_ERROR}{3}'
    assert obj.exception_name is None


def test_error_wrapper_exception_in_report():

    obj = DivNum(exception_name_in_detail=True)
    obj.div(1, 0)
    assert obj.error_detail == f'{ZeroDivisionError.__name__}{EXCEPTION_NAME_POSTFIX}{zero_division_error_text}'
    assert obj.error_status == f'{ERROR_STATUS_DETAIL_PREFIX}{ZeroDivisionError.__name__}{EXCEPTION_NAME_POSTFIX}{zero_division_error_text}'
    assert obj.exception_name == ZeroDivisionError.__name__
