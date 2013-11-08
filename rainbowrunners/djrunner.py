# -*- coding: utf-8 -*-

from django.test.runner import DiscoverRunner

from rainbowrunners.runner import NyanCatRunner

__all__ = (
    'NyanCatDiscoverRunner',
)


class NyanCatDiscoverRunner(DiscoverRunner):
    def run_suite(self, suite, **kwargs):
        return NyanCatRunner(
            failfast=self.failfast,
        ).run(suite)
