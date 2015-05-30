Wunderlist Workflow for Alfred
==========================

Create tasks in [Wunderlist](http://wunderlist.com) more effortlessly than ever before with this [Alfred 2](http://www.alfredapp.com/) workflow (requires Powerpack license). 

Setup
-----

### [Download here](https://raw.github.com/idpaterson/alfred-wunderlist-workflow/master/Wunderlist.alfredworkflow)

After downloading, simply double-click to install the workflow in Alfred. Use the `wl` command in Alfred to activate the workflow, or assign a hotkey in Alfred preferences. The workflow will guide you through securely logging in to Wunderlist and will even let you know when an important update is available.

Features you'll love
--------

The workflow provides an easy guided experience with tips along the way that will help you become a power user. 

The welcome screen appears when you've typed `wl` (and nothing else). Special commands are in the form `wl:command` with no space; once you type a space after `wl ` you're in task entry mode (at least for now, this is a bit harsh).
![Welcome screen](https://cloud.githubusercontent.com/assets/507058/7895432/791fe76e-065b-11e5-854c-5a0b29efab61.png)


### Adding tasks with due dates and recurrence

Add your first task! As you type, the workflow will pick out due dates and recurrence intervals in just about any format you could think of. Just write naturally, the due date, recurrence, and task text are updated in Alfred as you type.

![Task with due date and recurrence](https://cloud.githubusercontent.com/assets/507058/7895424/dd0e1ca6-065a-11e5-92c4-3d48ad0949cb.png)

Use the menus to configure your task until you become a power user capable of typing everything manually. It's so worthwhile to be able to drop tasks into Wunderlist in under a second.

![Due date menu](https://cloud.githubusercontent.com/assets/507058/7895423/d67861e4-065a-11e5-95fa-2bedeb70432b.png)

### Adding tasks to a specific list

To select a list, type it first followed by a colon or use the Change list menu item. No need to type the full list name, as long as you see the correct list in Alfred a few letters is usually sufficient.
![List by substring matching](https://cloud.githubusercontent.com/assets/507058/7895439/cc89462a-065b-11e5-89e9-8b1dfa52ac44.png)

### In sync

The workflow stays in sync with Wunderlist, so your lists (and tasks, in a later release) will be up-to-date and searchable. You can use the menu to select a list after typing the task. Just created a list in the Wunderlist app? No worries, it will show up in the workflow.
![List option](https://cloud.githubusercontent.com/assets/507058/7895446/1c1996c2-065c-11e5-9a8b-4e6cbd694ab9.png)
![List menu](https://cloud.githubusercontent.com/assets/507058/7895447/1d87f486-065c-11e5-9cf5-781d32a5c36c.png)

### Hints

Read the text below menu option and you'll be on your way to power user status – most menu items include helpful tips about how to apply a setting without navigating the menu. Finally, if you're using a dark theme it's probably a good idea to switch to light icons. Just go in through the main menu or jump straight to `wl:pref`
![Preferences](https://cloud.githubusercontent.com/assets/507058/7895453/719187fe-065c-11e5-938d-023368a7f67b.png)


Security
-----------

Your Wunderlist password is never made available to the workflow or stored in any way. Instead, when you log in through the Wunderlist portal you are asked to authorize the workflow to access your account. You can log out at any time through the `wl:pref` preferences screen.

Limitations
-----------

* No offline mode – the workflow must be able to connect the the API for each change you make; currently changes made while offline are not saved.
* Languages and date formats – the workflow only officially supports US English at this time. parsedatetime provides US English, UK English, Spanish, German, and Dutch with varying coverage of keywords (e.g. tomorrow, Tuesday) in each language; your mileage may vary with these languages. It is possible to add support for any local date format or language by installing some extra software, but there are a number of outstanding issues with adapting to generic locales.

Contributing
------------

So you want to help make this workflow better? That's great! <!-- Oops, the Python version does not have documentation yet.
Please see [the documentation](http://idpaterson.github.io/alfred-wunderlist-workflow/) for an introduction to the structure of this workflow.
-->After cloning the repository, run `npm install && grunt` to build the workflow. Open the Wunderlist-symlinked.alfredworkflow file to install a copy in Alfred that will update whenever you rebuild the workflow. After making a change, simply run `grunt build` to update the workflow then use Alfred to test. Using this process, the workflow is kept up-to-date while you work.

Always run through the semi-automated tests to ensure that your change does not cause issues elsewhere. When possible, add corresponding tests for your contributions.

Testing
-------

Unit tests are run automatically on every commit to reduce the likelihood of introducing a bug. Nevertheless, your feedback is crucial if anything seems to be broken.

Contributors can use the command `grunt test` to run the test suite and should do so to validate changes in any pull requests. If you add functionality, please back it with unit tests.

Acknowledgements
----------------

This workflow relies on the fantastic [Alfred-Workflow](https://github.com/deanishe/alfred-workflow) by [Dean Jackson](https://github.com/deanishe) to communicate with Alfred. The Alfred-Workflow library source code is bundled with the workflow and also included with the repository as a submodule.

Much of the natural language date processing is powered by [parsedatetime](https://github.com/bear/parsedatetime), a tremendously powerful date parser built by [Mike Taylor](https://github.com/bear) and various contributors. [Peewee](https://github.com/coleifer/peewee) by [Charles Leifer](https://github.com/coleifer) provides a simple interface to store and query synced data retrieved from Wunderlist using [Requests](https://github.com/kennethreitz/requests) by [Kenneth Reitz](https://github.com/kennethreitz). The source code of all three libraries is bundled with the workflow and each is included in the repository as a submodule.

Alternatives
------------

* [Wunderlist-3-Alfred](https://github.com/camgnostic/Wunderlist-3-Alfred) by [camgnostic](https://github.com/camgnostic)