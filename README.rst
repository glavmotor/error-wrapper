Error Wrapper
=============

Inheritance from the package's classes allows you to handle errors of any level in a uniform way and automatically log error messages if desired. This is a familiar routine, a fraction of which I wanted to reduce:)

* `Source on GitHub <http://github.com>`_

Installation
============

Install from PyPI with:

    pip install error-wrapper

Usage
=====
Completely abstract example:)

.. code:: python

    logger = logging.getLogger(__name__)

    class DivNum(ErrorWrapper):

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


    # Default creating params: report_prefix=None, exception_name_in_detail=False,
    #                          logger=None, auto_logging=False

    divnum_with_defaults = DevNum()

    divnum_with_auto_logging = DevNum(auto_logging=True, logger=logger)

    divnum_with_prefix_in_log_or_error_vessage = DevNum(report_prefix='DevNum instance error: ')

