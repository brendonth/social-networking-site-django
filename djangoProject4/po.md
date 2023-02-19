1. profiles
   - profile
    - relationship
    
2. posts
   -Post
   -comment
   -like
   -interest
   
3. allauth (authentication)

4. messages
   -message sent
   -message received

          <a href="{{ path_to_messages }}" class="{% if request.path == path_to_home  %}active{% endif %} item">
            Messages
        </a>