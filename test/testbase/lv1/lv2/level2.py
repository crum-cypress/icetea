"""
Copyright 2017 ARM Limited
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from icetea_lib.bench import Bench


class Testcase(Bench):

    def __init__(self):
        Bench.__init__(self, name="subsubdirtest",
                        title="Level 2 testcase test file",
                        status="maintenance",
                        purpose="dummy",
                        component=["None"],
                        type="smoke",
                        requirements={
                            "duts": {
                                '*': {
                                    "count": 0
                                    }
                                }
                            }
                        )

    def case(self):
        pass
