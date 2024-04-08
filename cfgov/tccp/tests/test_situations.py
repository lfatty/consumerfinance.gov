from itertools import product

from django.test import SimpleTestCase

from tccp.situations import (
    SITUATIONS,
    Situation,
    SituationFeatures,
    SituationSpeedBumps,
    get_situation_by_title,
)


class SituationTests(SimpleTestCase):
    def test_get_situation_by_title_valid(self):
        self.assertEqual(
            get_situation_by_title("Pay less interest"),
            SITUATIONS[0],
        )

    def test_get_situation_by_title_invalid(self):
        with self.assertRaises(KeyError):
            get_situation_by_title("invalid")

    def test_get_nonconflicting_params(self):
        self.assertEqual(
            Situation.get_nonconflicting_params(
                [
                    Situation("one", {"a": 1, "b": 2}),
                    Situation("two", {"c": [3, 4]}),
                    Situation("three", {"a": 5, "b": 2}),
                ]
            ),
            {"b": 2, "c": [3, 4]},
        )

    def test_get_get_nonconflicting_params_multiple_duplicates(self):
        self.assertEqual(
            Situation.get_nonconflicting_params(
                [
                    Situation("one", {"a": 1}),
                    Situation("two", {"a": 2}),
                    Situation("three", {"a": 1}),
                ]
            ),
            {},
        )


class SituationContentTests(SimpleTestCase):
    def test_situation_content(self):
        for situation, content in product(SITUATIONS, ["select", "results"]):
            with self.subTest(title=situation.title, content=content):
                self.assertTrue(getattr(situation, f"{content}_html"))


class SituationFeatureTests(SimpleTestCase):
    def test_no_combinations(self):
        features = SituationFeatures(
            [
                Situation("Pay less interest"),
                Situation("Foo"),
            ]
        )
        self.assertSequenceEqual(
            [s.title for s in features], ["Pay less interest", "Foo"]
        )

    def test_combination(self):
        features = SituationFeatures(
            [
                Situation("Pay less interest"),
                Situation("Make a big purchase"),
            ]
        )
        self.assertSequenceEqual(
            [s.title for s in features],
            ["Pay less interest Make a big purchase"],
        )


class SituationSpeedBumpTests(SimpleTestCase):
    def test_bumps(self):
        situations = [
            Situation("one", {"a": 1}),
            Situation("two", {"a": 2}, [{"content": "first"}]),
            Situation("three", {"a": 1}, [{"content": "second"}]),
        ]
        bumps = SituationSpeedBumps(situations)

        self.assertIsNone(bumps[0])
        self.assertIsNone(bumps[4])
        self.assertEqual(bumps[5], {"content": "first"})
        self.assertIsNone(bumps[9])
        self.assertEqual(bumps[10], {"content": "second"})
