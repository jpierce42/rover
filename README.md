# Rover Coding Project

The goal of this project to create a web interface for a database of dogs and their owners. You can use any language and frameworks you’d like to complete this project, but we'll best be able to evaluate your project if you write it using Django or Rails. While the project itself is simple, we're not just looking to see if you can complete the project. Please take your time and show us what you care about when you're writing software. The work you create here should be representative of code that we'd expect to receive from you if you were hired tomorrow.


### Requirements

1. A user should be able to create a dog, entering the dog's name, their owner's name, and a photo of the dog

2. The newly created dog should display in a list of all dogs

3. Each dog in the list should show their name and a thumbnail photo

4. The thumbnail image should be resized to maximum dimensions of 150x150 and retain the aspect ratio of the original image

5. Images should be resized on the server

6. When the user clicks on a dog, display a lightbox that shows:
  - The dog's name
  - The dog's owner's name
  - A larger version of the dog's photo

7. Allow the user to search for a dog by dog name or dog owner name.


Complete this project and push your solution back to this repository. When you're finished up, email your Rover contact and let them know.


---
### Comments from Jen:

App still in progress.  Currently you'll see the following features implemented:

- Basic app structure; models, views
- Form to add an owner & dog
- Image upload & thumbnail handling
- Some styling

Still in progress:

- Display dog detail page in lightbox rather than new page
- Search functionality
- Styling


Additionally, here are some Django-related questions I've come across as I learn about the framework.  I assume these are pretty basic question with straightforward answers; as mentioned, I'm brand new to Django!  Would be interested to hear the team's input on these.

- How do you decide when to use ModelForms?  Can you use a single form to edit two (or more) related models (e.g. dog and owner)?

- How do you avoid having to delete your entire database if you need to add a new column to a model? (This seems critical!)

- I didn't set up a production-ready solution for serving static files; looks like this is a fairly in-depth topic.  Would love to find out more about how you guys handle this.

- Speaking of static files, how do you organize multiple js, css, & image files for each app?  Ordinarily I'd create a subdirectory for each of these file types; I didn't immediately see how to do this in Django.

- Given more time, I'd make an effort to implement the thumbnail image resizing myself.  The actual image manipulation with PIL doesn't look super complicated, but I'm not sure how long it would take me to work out the right way to handle & save the thumbnail file in Django.  This is a pretty fair representation of my real-life development strategy; if I think something will be time-consuming and a good solution exists, I try not to reinvent the wheel.  But I'm sure I'm capable of figuring out a simple implementation myself, given more time.  We could look at this together in-person, if desired.