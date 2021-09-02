'''
A/B test generalizability

Listed below are a set of decisions that could be made when designing an A/B test. Identify the decision that would not cause an issue in generalizing the test results to the overall user population.

INSTRUCTIONS

Possible Answers:

o   Assigning users to the Test or Variant group based on their signup year. // False, your user base may evolve over time and this could potentially be introducing a bias.
*   Using a hash of the randomly assigned user id to determine user groupings. // Correct! This is a fine thing to do and a common way to tie the group a user belongs to to their identity.
o   Randomly assigning users within one country to different groups. // False, this would be generalizable to users within that country, but potentially not to users in other places.
o   Allowing users to change groups every time they use the service or software. // False, it would be impossible to then correlate the change in the user behavior to the treatment.
'''