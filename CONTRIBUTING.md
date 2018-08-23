# # Contributing to `Tarantulla-Twitter`

We'd love for you to contribute to our source code and to make `Tarantulla-twitter Module`
even better than it is today! Here are the guidelines we'd like you to follow:

- [Code of Conduct](#coc)
- [Question or Problem?](#question)
- [Issues and Bugs](#issue)
- [Feature Requests](#feature)
- [Documentation fixes](#docs)
- [Submission Guidelines](#submit)
- [Coding Rules](#rules)

## <a name="coc"></a> Code of Conduct
The `Tarantulla-twitter` is a module of Tarantulla, it was built to be a open and inclusive solution. So help us keep it this way. Please be kind to and respectful with other developers, as we all have the same goal: To make collecting, extracting and data-driven decisiton easier with `Tarantulla-twitter`. 
Our Code of Conduct complete [here][code-link]


## <a name="question"></a> Got an Module/Product Question or Problem?

If you have questions about how to use `Tarantulla-twitter`, please see our
[Readme][readme-link], and if you don't find the answer there, please contact
[hello@tarantulla.io](mailto:hello@tarantulla.io) with any issues you have.

## <a name="issue"></a> Found an Issue?

If you find a bug in the source code or a mistake in the documentation, you can help us by submitting [an issue][issue-link]. 

**Please see the [Submission Guidelines](#submit) below.**

### <a name="feature"></a> Want a Feature?

You can request a new feature by submitting an issue to our
[GitHub Repository][github]. If you would like to implement a new feature then consider what kind of change it is:

* **Major Changes** that you wish to contribute to the project should be
  discussed first with `Tarantulla-twitter` contributors in an issue or pull request so that we can develop a proper solution and better coordinate our efforts, prevent duplication of work, and help you to craft the change so that it is
  successfully accepted into the project.
* **Small Changes** can be crafted and submitted to the [GitHub Repository][github] as a Pull Request and just get it touch to our team and all contributors in an [new issue][issue-link].

### <a name="docs"></a> Want a Doc Fix?

If you want to help improve the docs, it's a good idea to let others know what you're working on to minimize duplication of effort. Create a [new issue][issue-link] (or comment on a related existing one) to let others know what you're working on.

For large fixes, please build and test the documentation before submitting the PR to be sure you haven't accidentally introduced layout or formatting issues.

If you want to help improve the docs at [New Issue][issue-link], please contact [hello@tarantulla.io](mailto:hello@tarantulla.com).

## <a name="submit"></a> Submission Guidelines

### Submitting an Issue
Before you submit your issue search the archive, maybe your question was already answered.

* **Type of Issue** - bugs report, documentation fixed, feature request
* **Overview of the Issue** - if an error is being thrown a non-minified stack trace helps
* **Operating System (when relevant)** 
	- If your OS is different of Linux
	- if you use linux, what is the distribution of it?
* **Reproduce the Error** -  provide an isolated code snippet or an unambiguous set of steps and no code repetition.
* **Related Issues** - has a similar issue been reported before?
* **Suggest a Fix** - if you can't fix the bug yourself, perhaps you can point to what might be causing the problem (line of code or commit)


### Submitting a Pull Request
Before you submit your pull request consider the following guidelines:

* Search [GitHub][github] for an open or closed Pull Request that relates to
  your submission. You don't want to duplicate effort.
* Make your changes in a new git branch:

    ```shell
    git checkout -b my-fix-branch master
    ```

* Create your patch, **including appropriate test cases**.
* Follow our [Coding Rules](#rules).
* Run the full `Tarantulla-twitter` test suite (aliased by `make test`), and ensure
  that all tests pass.
* Commit your changes using a descriptive commit message.

    ```shell
    git commit -a
    ```
  Note: the optional commit `-a` command line option will automatically "add"
  and "rm" edited files.

* Build your changes locally to ensure all the tests pass:

    ```shell
    make test
    ```

* Push your branch to GitHub:

    ```shell
    git push origin my-fix-branch
    ```

In GitHub, send a pull request to `Tarantulla-twitter:master`.
If we suggest changes, then:

* Make the required updates.
* Re-run the `Tarantulla-twitter` test suite to ensure tests are still passing.
* Commit your changes to your branch (e.g. `my-fix-branch`).
* Push the changes to your GitHub repository (this will update your Pull Request).

That's it! Thank you for your contribution!

#### After your pull request is merged

After your pull request is merged, you can safely delete your branch and pull the changes from the main (upstream) repository.

## <a name="rules"></a> Coding Rules

To ensure consistency throughout the source code, keep these rules in mind as you are working:

* All features or bug fixes **must be tested** by one or more tests.
* All classes and methods **must be documented**.

Check the Tarantulla [landing page][page-link].

[readme-link]: https://github.com/oncase/tarantulla-twitter/blob/master/README.md
[issue-link]: https://github.com/oncase/tarantulla-twitter/issues/new
[github]: https://github.com/oncase/tarantulla-twitter/
[code-link]: https://github.com/oncase/tarantulla-twitter/blob/master/CODE_OF_CONDUCT.md
[page-link]: https://tarantulla.io/
