# -*- coding: utf-8 -*-

import sys
import time
import unittest
import warnings

from rainbowrunners.result import NyanCatResult
from rainbowrunners.utils import Colors

__all__ = (
    'NyanCatRunner',
)


class BaseRainbowRunner(object):
    resultclass = None

    def __init__(self, stream=None, descriptions=True,
                 failfast=False, buffer=False, warnings=None):
        if stream is None:
            stream = sys.stderr
        self.stream = unittest.runner._WritelnDecorator(stream)
        self.descriptions = descriptions
        self.failfast = failfast
        self.buffer = buffer
        self.warnings = warnings

    def _makeResult(self):
        return self.resultclass(stream=self.stream, descriptions=self.descriptions)

    def run(self, test):
        result = self._makeResult()
        unittest.registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer

        with warnings.catch_warnings():
            if self.warnings:
                warnings.simplefilter(self.warnings)
                if self.warnings in ('default', 'always',):
                    warnings.filterwarnings(
                        'module', category=DeprecationWarning,
                        message='Please use assert\w+ instead.'
                    )
            start_time = time.time()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()
            try:
                test(result)
            finally:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()
            stop_time = time.time()

        time_taken = stop_time - start_time
        result.printErrors()

        if hasattr(result, 'separator2'):
            self.stream.writeln(result.separator2)

        run = result.testsRun
        self.stream.writeln('\033[{0}mRan {1} test{2} in {3:.3}s\033[0m'.format(
            Colors.RESULT, run, run != 1 and 's' or '', time_taken
        ))
        self.stream.writeln()

        expected_fails = unexpected_successes = skipped = 0
        try:
            results = map(len, (result.expectedFailures,
                                result.unexpectedSuccesses,
                                result.skipped))
        except AttributeError:
            pass
        else:
            expected_fails, unexpected_successes, skipped = results

        infos = []
        if not result.wasSuccessful():
            self.stream.write('\033[{0}mFAILED\033[0m'.format(Colors.ERROR))
            failed, errored = len(result.failures), len(result.errors)
            if failed:
                infos.append('failures={0}'.format(failed))
            if errored:
                infos.append('errors={0}'.format(errored))
        else:
            self.stream.write('\033[{0}mOK\033[0m'.format(Colors.SUCCESS))

        if skipped:
            infos.append('skipped={0}'.format(skipped))
        if expected_fails:
            infos.append('expected failures={0}'.format(expected_fails))
        if unexpected_successes:
            infos.append('unexpected successes={0}'.format(unexpected_successes))

        if infos:
            self.stream.writeln(' ({0})'.format(', '.join(infos)))
        else:
            self.stream.writeln()

        return result


class NyanCatRunner(BaseRainbowRunner):
    resultclass = NyanCatResult
