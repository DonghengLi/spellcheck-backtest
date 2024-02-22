# Spellcheck Backtest Script

1. Download data using [this query](https://portal.azure.com#@301f59c4-c269-4a66-8a8c-f5daab211fa3/blade/Microsoft_OperationsManagementSuite_Workspace/Logs.ReactView/resourceId/%2Fsubscriptions%2Fbd26395a-031e-498b-acfe-4066c3b64edf%2FresourceGroups%2Fsaas-xhis-prod%2Fproviders%2Fmicrosoft.insights%2Fcomponents%2Fsaas-xhis-appinsight-cc-prod/source/LogsBlade.AnalyticsShareLinkToQuery/q/H4sIAAAAAAAAA9VWS2%252FbOBC%252B%252B1ewvphCLT%252FSoti66wWybbHIoSen6KFYCAw5tplIpEpS26SP%252F96hJEuk5QTddC9r2DA4nPc3M5wcHBHsLhPMAVkT%252F%252BdkAfRscfY8XSzTs9%252BSV6O8YbLI8GwhmrPnykAJpF1JlTFHD7JZrjnLM6ezynF6UD4lk3Mr2fySyRLkJCFPyVJM619ndPlitVjgN0kCG1ewkwqtdAbT2peGg1fW6eLtP6Cc%252FTOvfAisLOnYMmbT2720KR6lsnK3dynnaWm0GCezUGyo6C8DoH5GU8qZYubupMJPFZg6coaaaHi%252FoooVsLLOSLWb1nFZx4pydcjDlFQWTHYhOp5G%252FA3eoQNa2ZW4Qx2SJwn5OnD%252FtS5KpMFbxXWlHBiyHoX3o2%252Fk8x4MEO8GWa%252FJhLcSKRxEJh1T5x75Yx0CwhCJ%252Fu73Dh4UhFvncbIOyswDp5swaMmMhezaakU72nFkMxQ2LElmXjrpvGh1oa%252BH6C4NMIdSbjaId9L70AV0IUJPhlZ7Pm%252FUVkXBjPwShr8mBbul3TkhV3ehepS61piXG6nEWiqFaacjgp8o9Z7w6MyGwgfsxqyUqQL3WZubtASz1aZgisO4VtPWEXmCaunkfPN%252BM%252FF9ePF6gw04n5N7hEmudxZzzowDQbZGF%252BRsSd4xw%252FcEB8Ozaa1caVIa2MpbMico6ZVlWyAUZrsZmfNSw1wImbRuHwDx8GIu%252F00tRIHXtFll8jr6opjbEvKc74HfjI9MPQb7SIPQ3GFgDwk3LL1k42Qr%252BATrdVLnKvSlprbsQlonFXdRJSVEq4jQTJQ9jp7cj5%252F7%252BvkRrXpUTFazMgUh0fnx6Ncwi%252FHy%252FVtbqEo%252F5fpBk9bwpTV%252BqQFb5W78y%252B3bSncJA%252FFBG%252BGfr8Ybh39RlzOzy6Lung6EB%252F3egNJRNueX%252F2dcAhia0dHcS9u%252FIp7akrWRGADLN14KzfmaHodyXBsDHHMXc%252FyHg7mzcIC2YDe4emA%252F0dM%252BPjiwt1We68pH2XfZURN%252Bw2mnr9HkqbqS2y2VVqEWOigcXHCa15p%252B%252FDs5UVjTYSyBuvjuWNngNs6r1xNRPAgR0zI69eXBjMHFLQe1c%252FthSB7NBfEzP2Q7cqZmwjZ5cDc58WxGLTUAoa2f8F1u98%252BgeeOt8uVy4VfZxZL0C%252Bbo%252B6tRv6LR4z3SJ6JSWIHkHqZ6R0xO%252B9Mtwrj%252F%252BjW43odD9%252BJNOKisgCeIelgzx8D%252FANci%252FhTGCwAA).

2. Run `python src/main.py <path to the query result> <path to the output result> [loaded dictionaries]`. Loaded dictionaries are optional, currently supported `medical_abbreviations`, `wordlist_medicalterms_en`, and `dsat_case`. You can load several dictionaries by concating them using `+` operator (e.g. `dsat_case+medical_abbreviations`)

## Adding a dictionary

Add an entry to the `DICTIONARY` variable in `src/main.py`, mapping the dictionary name to the function that loads the dictionary. The dictionary loading function should take a set of string argument and adds the word into the set.
