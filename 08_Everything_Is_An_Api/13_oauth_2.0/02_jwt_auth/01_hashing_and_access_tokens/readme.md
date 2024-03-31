## JWT

It's a standard to codify a JSON object in a long dense string without spaces. It is not encrypted, so, anyone could recover the information from the contents.

But it's signed. So, when you receive a token that you emitted, you can verify that you actually emitted it.

That way, you can create a token with an expiration of, let's say, 1 week. And then when the user comes back the next day with the token, you know that user is still logged in to your system.

After a week, the token will be expired and the user will not be authorized and will have to sign in again to get a new token. And if the user (or a third party) tried to modify the token to change the expiration, you would be able to discover it, because the signatures would not match.

If you want to play with JWT tokens and see how they work, check https://jwt.io.

JWS payload
The payload contains statements about the entity (typically, the user) and additional entity attributes, which are called claims. In this example, our entity is a user.

When working with JWT claims, you should be aware of the different claim types and naming rules.
https://datatracker.ietf.org/doc/html/rfc7519#section-4.1


## JWT consists of three  things

1. Header
2. Payload
3. Secret_Key