# Laptop Nation: Elizabeth, Anthony, Maya
SoftDev
K19 - Session/Cookies
2022-11-04
time spent: 1 hr

### DISCO:
- We realized we approached it the wrong way at first, and stored the hardcoded login info in session. It should remain in the backend code.
- session.pop() takes in a key in session
- We can have multiple render_template()'s for a single route to perform different tasks
- return redirect() returns a redirect to the route given

### QCC:
- How does the secret key get generated/used?
- Can we redirect without flask.redirect()?