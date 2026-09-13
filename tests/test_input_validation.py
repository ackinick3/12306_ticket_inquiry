import unittest
from datetime import date

from input_validation import prompt_date, prompt_station, validate_date, validate_station


class ValidateDateTests(unittest.TestCase):
    def test_rejects_wrong_date_format(self):
        with self.assertRaisesRegex(ValueError, "日期格式错误"):
            validate_date("2026/09/13", today=date(2026, 9, 13))

    def test_rejects_nonexistent_date(self):
        with self.assertRaisesRegex(ValueError, "日期不存在"):
            validate_date("2026-02-30", today=date(2026, 1, 1))

    def test_rejects_past_date(self):
        with self.assertRaisesRegex(ValueError, "日期已过期"):
            validate_date("2026-09-12", today=date(2026, 9, 13))

    def test_accepts_today(self):
        self.assertEqual(
            validate_date("2026-09-13", today=date(2026, 9, 13)),
            "2026-09-13",
        )


class ValidateStationTests(unittest.TestCase):
    def test_rejects_unknown_station_with_field_name(self):
        with self.assertRaisesRegex(ValueError, "出发站不存在"):
            validate_station("不存在站", {"上海": "SHH"}, "出发站")

    def test_returns_the_station_code(self):
        self.assertEqual(
            validate_station("上海", {"上海": "SHH"}, "出发站"),
            "SHH",
        )


class PromptUntilValidTests(unittest.TestCase):
    def test_date_error_is_reported_before_retrying(self):
        answers = iter(["2026/09/13", "2026-09-13"])
        messages = []

        result = prompt_date(
            input_func=lambda _: next(answers),
            output_func=messages.append,
            today=date(2026, 9, 13),
        )

        self.assertEqual(result, "2026-09-13")
        self.assertEqual(messages, ["日期格式错误，请使用 YYYY-MM-DD 格式。"])

    def test_unknown_station_is_reported_before_retrying(self):
        answers = iter(["不存在站", "上海"])
        messages = []

        result = prompt_station(
            {"上海": "SHH"},
            "出发站",
            input_func=lambda _: next(answers),
            output_func=messages.append,
        )

        self.assertEqual(result, "SHH")
        self.assertEqual(messages, ["出发站不存在，请重新输入。"])


if __name__ == "__main__":
    unittest.main()
