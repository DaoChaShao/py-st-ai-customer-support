**INTRODUCTION**  
This application is designed to help vocational students understand classic technical concepts in AI customer support.

**INSTRUCTIONS FOR USING THE APPLICATION**

1. Clone the repository to your local machine.
2. Install the required dependencies with the command `pip install -r requirements.txt`.
3. Run the application with the command `streamlit run main.py`.
4. You can also try the application by visiting the following
   link: [![Static Badge](https://img.shields.io/badge/Open%20in%20Streamlit-Daochashao-red?style=for-the-badge&logo=streamlit&labelColor=white)](https://ai-customer-support.streamlit.app/)

**LICENCE**  
This application is licensed under the [BSD-3-Clause License](LICENSE). You can click the link to read the licence.

**INSTRUCTIONS FOR CREATING CHANGELOG**

1. Install the required dependencies with the command `pip install git-changelog`.
2. Prepare the configuration file of `pyproject.toml` at the root of the file.
3. Run the command `pip show git-changelog` to check whether the changelog package has been installed and its version.
4. The changelog style is [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
5. Run the command `git-changelog`, creating the `Changelog.md` file.
6. Add the file `Changelog.md` to version control with the command `git add Changelog.md` or using the UI interface.
7. Run the command `git-changelog --output CHANGELOG.md` committing the changes and updating the changelog.
8. Push the changes to the remote repository with the command `git push origin main` or using the UI interface.