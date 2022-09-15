<p align='center'>
<img width="200" src="static/images/pg.svg" alt="PRODY KA LOGO">
</p>
<h1 align='center'>PRODYOGIKI'23</h1>
This website is using django backend. All you need to do is to go through https://docs.djangoproject.com/ so that you get the basic knowledge that how things are working in django.

## Steps to follow :pencil2::

1. First of all install Django:

```bash
  python -m pip install Django
```

2. Clone the repository:

```bash
git clone https://github.com/lucifer1708/prody-2023.git
```

3. Change the directory to prody-2023 using:

```bash
cd prody-2023
```

4. Create a virtual environment:

```bash
pip install virtualenv
virtualenv venv
```

5. Activate the virtual environment

```bash
source venv/bin/activate
```

6. Now install all the packages which are being used in this project:

```bash
pip install -r requirements.txt
```

7. Now run the development server:

```bash
python manage.py runserver
```

### Alternative:

```bash
docker-compose up
```
and navigate to localhost:8000


## Roadmap :earth_asia:

- Adding signup login stuff (:heavy_check_mark:)
- Email Confirmation for registering accounts (:heavy_check_mark:)
- Adding Models to show events (:heavy_check_mark:)
- Adding Models to register events (:heavy_check_mark:)
- Adding Profile page for user (:heavy_check_mark:)
- Adding Sponsor Model (:heavy_check_mark:)
- Adding Other Features(:x:)

## File Structure
.
├── docker-compose.yml
├── Dockerfile
├── events
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── prody
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── requirements.txt
├── static
│   ├── assets
│   │   ├── css
│   │   │   ├── bootstrap.min.css
│   │   │   └── font-awesome.min.css
│   │   ├── fonts
│   │   │   └── font-awesome-4.7.0
│   │   │       ├── css
│   │   │       │   ├── font-awesome.css
│   │   │       │   └── font-awesome.min.css
│   │   │       └── fonts
│   │   │           ├── FontAwesome.otf
│   │   │           ├── fontawesome-webfont.eot
│   │   │           ├── fontawesome-webfont.svg
│   │   │           ├── fontawesome-webfont.ttf
│   │   │           ├── fontawesome-webfont.woff
│   │   │           └── fontawesome-webfont.woff2
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       ├── jquery-3.2.1.min.js
│   │       └── popper.min.js
│   ├── css
│   │   ├── bootstrap
│   │   │   ├── _media.css
│   │   │   ├── mixins
│   │   │   │   ├── _border-radius.css
│   │   │   │   ├── _reset-text.css
│   │   │   │   ├── _screen-reader.css
│   │   │   │   ├── _text-hide.css
│   │   │   │   └── _visibility.css
│   │   │   └── utilities
│   │   │       └── _stretched-link.css
│   │   ├── bootstrap.min.css
│   │   ├── event-style.css
│   │   ├── navbar.css
│   │   ├── profile.css
│   │   ├── sponsor.css
│   │   └── style.css
│   ├── images
│   │   ├── avatars
│   │   │   └── default-profile-picture.png
│   │   ├── bg.jpg
│   │   ├── pg.svg
│   │   └── prody1.png
│   ├── js
│   │   ├── bootstrap.min.js
│   │   ├── jquery.min.js
│   │   ├── main.js
│   │   ├── navbar.js
│   │   ├── popper.js
│   │   └── profile.js
│   └── scss
│       ├── bootstrap
│       │   ├── _alert.scss
│       │   ├── _badge.scss
│       │   ├── bootstrap-grid.scss
│       │   ├── bootstrap-reboot.scss
│       │   ├── bootstrap.scss
│       │   ├── _breadcrumb.scss
│       │   ├── _button-group.scss
│       │   ├── _buttons.scss
│       │   ├── _card.scss
│       │   ├── _carousel.scss
│       │   ├── _close.scss
│       │   ├── _code.scss
│       │   ├── _custom-forms.scss
│       │   ├── _dropdown.scss
│       │   ├── _forms.scss
│       │   ├── _functions.scss
│       │   ├── _grid.scss
│       │   ├── _images.scss
│       │   ├── _input-group.scss
│       │   ├── _jumbotron.scss
│       │   ├── _list-group.scss
│       │   ├── _media.scss
│       │   ├── mixins
│       │   │   ├── _alert.scss
│       │   │   ├── _background-variant.scss
│       │   │   ├── _badge.scss
│       │   │   ├── _border-radius.scss
│       │   │   ├── _box-shadow.scss
│       │   │   ├── _breakpoints.scss
│       │   │   ├── _buttons.scss
│       │   │   ├── _caret.scss
│       │   │   ├── _clearfix.scss
│       │   │   ├── _deprecate.scss
│       │   │   ├── _float.scss
│       │   │   ├── _forms.scss
│       │   │   ├── _gradients.scss
│       │   │   ├── _grid-framework.scss
│       │   │   ├── _grid.scss
│       │   │   ├── _hover.scss
│       │   │   ├── _image.scss
│       │   │   ├── _list-group.scss
│       │   │   ├── _lists.scss
│       │   │   ├── _nav-divider.scss
│       │   │   ├── _pagination.scss
│       │   │   ├── _reset-text.scss
│       │   │   ├── _resize.scss
│       │   │   ├── _screen-reader.scss
│       │   │   ├── _size.scss
│       │   │   ├── _table-row.scss
│       │   │   ├── _text-emphasis.scss
│       │   │   ├── _text-hide.scss
│       │   │   ├── _text-truncate.scss
│       │   │   ├── _transition.scss
│       │   │   └── _visibility.scss
│       │   ├── _mixins.scss
│       │   ├── _modal.scss
│       │   ├── _navbar.scss
│       │   ├── _nav.scss
│       │   ├── _pagination.scss
│       │   ├── _popover.scss
│       │   ├── _print.scss
│       │   ├── _progress.scss
│       │   ├── _reboot.scss
│       │   ├── _root.scss
│       │   ├── _spinners.scss
│       │   ├── _tables.scss
│       │   ├── _toasts.scss
│       │   ├── _tooltip.scss
│       │   ├── _transitions.scss
│       │   ├── _type.scss
│       │   ├── utilities
│       │   │   ├── _align.scss
│       │   │   ├── _background.scss
│       │   │   ├── _borders.scss
│       │   │   ├── _clearfix.scss
│       │   │   ├── _display.scss
│       │   │   ├── _embed.scss
│       │   │   ├── _flex.scss
│       │   │   ├── _float.scss
│       │   │   ├── _overflow.scss
│       │   │   ├── _position.scss
│       │   │   ├── _screenreaders.scss
│       │   │   ├── _shadows.scss
│       │   │   ├── _sizing.scss
│       │   │   ├── _spacing.scss
│       │   │   ├── _stretched-link.scss
│       │   │   ├── _text.scss
│       │   │   └── _visibility.scss
│       │   ├── _utilities.scss
│       │   ├── _variables.scss
│       │   └── vendor
│       │       └── _rfs.scss
│       └── style.scss
├── templates
│   ├── account
│   │   ├── account_inactive.html
│   │   ├── base.html
│   │   ├── email
│   │   │   ├── base_message.txt
│   │   │   ├── email_confirmation_message.txt
│   │   │   ├── email_confirmation_signup_message.txt
│   │   │   ├── email_confirmation_signup_subject.txt
│   │   │   ├── email_confirmation_subject.txt
│   │   │   ├── password_reset_key_message.html
│   │   │   ├── password_reset_key_subject.txt
│   │   │   ├── unknown_account_message.txt
│   │   │   └── unknown_account_subject.txt
│   │   ├── email_confirm.html
│   │   ├── email.html
│   │   ├── login.html
│   │   ├── logout.html
│   │   ├── messages
│   │   │   ├── cannot_delete_primary_email.txt
│   │   │   ├── email_confirmation_sent.txt
│   │   │   ├── email_confirmed.txt
│   │   │   ├── email_deleted.txt
│   │   │   ├── logged_in.txt
│   │   │   ├── logged_out.txt
│   │   │   ├── password_changed.txt
│   │   │   ├── password_set.txt
│   │   │   ├── primary_email_set.txt
│   │   │   └── unverified_primary_email.txt
│   │   ├── password_change.html
│   │   ├── password_reset_done.html
│   │   ├── password_reset_from_key_done.html
│   │   ├── password_reset_from_key.html
│   │   ├── password_reset.html
│   │   ├── password_set.html
│   │   ├── signup_closed.html
│   │   ├── signup.html
│   │   ├── snippets
│   │   │   └── already_logged_in.html
│   │   ├── verification_sent.html
│   │   └── verified_email_required.html
│   ├── admin
│   │   ├── actions.html
│   │   ├── app_index.html
│   │   ├── auth
│   │   │   └── user
│   │   │       ├── add_form.html
│   │   │       └── change_password.html
│   │   ├── base.html
│   │   ├── base_site.html
│   │   ├── change_form.html
│   │   ├── change_form_object_tools.html
│   │   ├── change_list.html
│   │   ├── change_list_object_tools.html
│   │   ├── change_list_results.html
│   │   ├── date_hierarchy.html
│   │   ├── delete_confirmation.html
│   │   ├── delete_selected_confirmation.html
│   │   ├── edit_inline
│   │   │   ├── stacked.html
│   │   │   └── tabular.html
│   │   ├── filer
│   │   │   ├── breadcrumbs.html
│   │   │   ├── change_form.html
│   │   │   ├── delete_selected_files_confirmation.html
│   │   │   ├── file
│   │   │   │   └── change_form.html
│   │   │   ├── folder
│   │   │   │   ├── change_form.html
│   │   │   │   └── directory_listing.html
│   │   │   ├── image
│   │   │   │   └── change_form.html
│   │   │   └── tools
│   │   │       └── detail_info.html
│   │   ├── filter.html
│   │   ├── import_export
│   │   │   ├── base.html
│   │   │   ├── change_list_export.html
│   │   │   ├── change_list_export_item.html
│   │   │   ├── change_list.html
│   │   │   ├── change_list_import_export.html
│   │   │   ├── change_list_import.html
│   │   │   ├── change_list_import_item.html
│   │   │   ├── export.html
│   │   │   └── import.html
│   │   ├── includes
│   │   │   ├── fieldset.html
│   │   │   └── object_delete_summary.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── mptt_filter.html
│   │   ├── object_history.html
│   │   ├── pagination.html
│   │   ├── popup_response.html
│   │   ├── search_form.html
│   │   ├── solo
│   │   │   ├── change_form.html
│   │   │   └── object_history.html
│   │   └── submit_line.html
│   ├── admin_doc
│   │   ├── base_docs.html
│   │   ├── bookmarklets.html
│   │   ├── index.html
│   │   ├── missing_docutils.html
│   │   ├── model_detail.html
│   │   ├── model_index.html
│   │   ├── template_detail.html
│   │   ├── template_filter_index.html
│   │   ├── template_tag_index.html
│   │   ├── view_detail.html
│   │   └── view_index.html
│   ├── base.html
│   ├── events
│   │   ├── event.html
│   │   ├── event.old.html
│   │   └── sponsors.html
│   ├── includes
│   │   └── navbar.html
│   ├── jazzmin
│   │   ├── includes
│   │   │   ├── carousel.html
│   │   │   ├── collapsible.html
│   │   │   ├── horizontal_tabs.html
│   │   │   ├── related_modal.html
│   │   │   ├── single.html
│   │   │   ├── ui_builder_panel.html
│   │   │   └── vertical_tabs.html
│   │   └── widgets
│   │       └── select.html
│   ├── layouts
│   │   └── base.html
│   ├── modals
│   │   ├── add-event.html
│   │   ├── base.html
│   │   ├── index.html
│   │   └── _modal.html
│   ├── registration
│   │   ├── base.html
│   │   ├── logged_out.html
│   │   ├── password_change_done.html
│   │   ├── password_change_form.html
│   │   ├── password_reset_complete.html
│   │   ├── password_reset_confirm.html
│   │   ├── password_reset_done.html
│   │   └── password_reset_form.html
│   └── users
│       ├── home.html
│       ├── profile-edit.html
│       └── profile.html
└── users
    ├── adapters.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── __init__.py
    ├── models.py
    ├── signals.py
    ├── urls.py
    └── views.py

50 directories, 275 files

## My choice for coding :stuck_out_tongue:

<p align='center'>
<img width="200" src="https://github.com/vim/vim/raw/master/runtime/vimlogo.gif" alt="VIM KA LOGO">
</p>
