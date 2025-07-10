<!-- insertion marker -->
<a name="0.1.0"></a>

## [0.1.0](https://github.com///compare/814c52306db7adf9e1f48021419593068b2de6af...0.1.0) (2025-07-10)

### Features

- enhance application information display with detailed module descriptions ([e999079](https://github.com///commit/e9990799a5b8089a28c724b6eac1a44a9b3f7eac))
- add DeepSeekCompleter class and update client methods for improved API integration ([967b1a4](https://github.com///commit/967b1a407c6975f2f4e9670cec04fedbc7bd6e68))
- implement intent classification interface with DeepSeek integration ([06d62ed](https://github.com///commit/06d62ed782095382b10eb505f33a3848f10fa875))
- add deepseek_api_model function for language model integration ([2a5a962](https://github.com///commit/2a5a962f54fdb2b0e4765b024997ecc04044fabb))
- add personalised_response function to generate tailored customer replies ([16456dd](https://github.com///commit/16456ddee2eedf14763104d66704134857ecee8d))
- implement personalized response interface with OpenAI API integration ([f1d92e3](https://github.com///commit/f1d92e3437799579135c1d2e38ba577351ab3004))
- implement intent classification interface with OpenAI integration ([82213b1](https://github.com///commit/82213b147bf46503a57066c593479772f8c77e0e))
- add data.py with predefined customer questions and intent categories ([ce074be](https://github.com///commit/ce074becc322340196ef5854ffa3f64bfa30a8f0))
- add intent recognizer function to classify customer questions ([67b64bc](https://github.com///commit/67b64bc2e8d291daafdcb0dfaa8a93af168b93b0))
- add OpenAI API wrappers for embeddings and completions ([baa4d57](https://github.com///commit/baa4d57977d62b548184d98a4e2e57a79a1de539))
- add d_intent_deepseek.py with main function template ([4d94dd5](https://github.com///commit/4d94dd5d3e511c9b4f06dea2f5cc3fa347e0911f))
- update requirements.txt to include additional libraries for data processing and visualization ([0365241](https://github.com///commit/0365241cfc1d1a0457bd3c9a7cb4d0c4b9ff693c))
- add dimensionality reduction and visualization functions using t-SNE and Plotly ([b607b7a](https://github.com///commit/b607b7a3e3be7bd259b6f1f4b2fa76cb46463051))
- implement semantic understanding interface with OpenAI API integration ([3aa8a07](https://github.com///commit/3aa8a072c2e4d8c9ab249c7bcd13b6fc0c43f705))
- add Timer class to measure elapsed time ([416ef2b](https://github.com///commit/416ef2b53dfc98c61ccfcedd3bb0d35c18a9166c))
- remove main function and entry point from b_understand.py ([dd85d51](https://github.com///commit/dd85d517c2935059d6033dbb1a814c2e1ce3e01b))
- add z_about.py with main function template ([d0a2f37](https://github.com///commit/d0a2f37f5ecab420468a28554cb5cf043727a0ee))
- add Streamlit dependency to requirements.txt ([cb9282a](https://github.com///commit/cb9282a49a755f067aa65f3f79e7301fcf86dfc4))
- implement main function to configure Streamlit application ([549d4d1](https://github.com///commit/549d4d1b335df2c19c93424752591859947d6406))
- add layout.py for Streamlit application configuration and navigation ([5a839a1](https://github.com///commit/5a839a1adc728ed16134ebeaf78c1cbe7d4d62bc))
- add helper.py with main function template ([dccbd9f](https://github.com///commit/dccbd9f242693c32b5fd1291d80549dfc86b9df4))
- add d_response.py with main function template ([3c3e3dd](https://github.com///commit/3c3e3dd6358c089fb4b71e2daa14edc22b37dcd7))
- add c_intent.py with main function template ([9e85912](https://github.com///commit/9e859126b093623d1c45cef4b884fc1d9145d91f))
- add b_understand.py with main function template ([eee897c](https://github.com///commit/eee897c695d3d80de576dd0512fed2e6c215bf41))
- add initial Streamlit application for Smart Chat Lab ([72c8936](https://github.com///commit/72c8936183252d37c6be2663ce0be40fe0090b61))
- add main.py with initial function structure ([e17a9ca](https://github.com///commit/e17a9ca3614f1c71001803dfa0ba48760fee5bf7))

### Bug Fixes

- correct spelling of "Personalized" to "Personalised" in layout.py ([3ae399b](https://github.com///commit/3ae399b69fd4901b0280e7bf6aa6afb4ff372aba))
- update typo in the list of personalised questions. ([5375216](https://github.com///commit/5375216249fd0b331ea55c61bda6722c7b2ac4c0))
- rename variable for OpenAI API key and update validation checks ([d509133](https://github.com///commit/d509133a1b308451c97d35ecff9ea0093f89e661))
- update button properties in b_understand.py for improved UI interaction ([e6cfcf0](https://github.com///commit/e6cfcf0892fe984c5a833a1f95b3250ae08e8546))
- update layout.py to reflect renamed files and adjust section titles ([2d09785](https://github.com///commit/2d09785cd4bf4597c55364af3b6272e32a93758b))
- rename d_response.py to e_response.py for consistency ([547a49a](https://github.com///commit/547a49ab14c9b9de19bb65ae7b8a44eebbf98a5e))
- rename c_intent.py to c_intent_openai.py for clarity ([92afd1b](https://github.com///commit/92afd1bbbe88d68662ba35aeee8b5868cd52c754))
- rename "Parameters" to "OpenAI Parameters" and update button help text in b_understand.py ([22bfa6b](https://github.com///commit/22bfa6b04a133a143dc62879eb22756dc9595b99))
- update Python version in introduction and modify empty message text in a_home.py ([cebb11d](https://github.com///commit/cebb11dfe18be392686d92237ab5909f4b697ae1))
- rename "About" section to "Information" in layout.py ([7ecb6c5](https://github.com///commit/7ecb6c5ed735d5a935aa6141c7121c6805523287))

### Chore

- add missing newline in b_understand.py for code formatting ([6992d8b](https://github.com///commit/6992d8b0fa4c5dc34cfc771038989f2da931eae5))
- update CHANGELOG.md with recent feature additions and bug fixes ([f908102](https://github.com///commit/f9081021855d7a48e365b3edaa0c2e7aa99d3396))
- update CHANGELOG.md for version 0.1.0 ([3e089ab](https://github.com///commit/3e089ab03146b9b3e4c8d91ba9147a5f9a48934a))
- create CHANGELOG.md for version 0.1.0 ([862986d](https://github.com///commit/862986dae0c77529c2e954dbd8ff4ad7ab6cc44e))
- add git-changelog dependency to requirements.txt ([b6fdded](https://github.com///commit/b6fdded0b798a539ca75186671a365afa975bd88))
- add pyproject.toml for changelog configuration ([89dc9db](https://github.com///commit/89dc9db3a7f088adb8b55a36f89ff564b00077d6))
- add requirements.txt for project dependencies ([303d30c](https://github.com///commit/303d30c4d83fac5994ecfc8633117b05a3737a5c))

### Docs

- update CHANGELOG.md for version 0.1.0 ([131f5dc](https://github.com///commit/131f5dc7cdaf070409f55954179bc48357e06cbe))
- update changelog instructions in README.md ([eaf4741](https://github.com///commit/eaf4741e34bec9a757d3373d5c24965fa9ed7836))
- update README.md with additional instructions for changelog creation ([46f778a](https://github.com///commit/46f778a337edd335f4a5481a26a6780f1c77c4fb))
- update README.md with changelog and application usage instructions ([fdd8b45](https://github.com///commit/fdd8b45e48ab4baea720f0b0d72aafd32eadd6a1))
- add README.md with application introduction and changelog instructions ([eb6237c](https://github.com///commit/eb6237c64e02b84e7f3b678b299ee4b811d629be))

