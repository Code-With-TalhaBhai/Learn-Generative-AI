[
{'role': 'user',
  'content': "What's the weather like in San Francisco, Tokyo, and Paris?"},
 'ChatCompletionMessage'(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_fNnYBoRGqfhWK4r7FUJo6BNu', function=Function(arguments='{"location": "San Francisco", "unit": "celsius"}', name='get_current_weather'), type='function'), ChatCompletionMessageToolCall(id='call_wzBuswuw0Wk47qleUmFCu2GZ', function=Function(arguments='{"location": "Tokyo", "unit": "celsius"}', name='get_current_weather'), type='function'), ChatCompletionMessageToolCall(id='call_dU3wwhoDo7oVkSQyQIdJkyG6', function=Function(arguments='{"location": "Paris", "unit": "celsius"}', name='get_current_weather'), type='function')]),
 {'tool_call_id': 'call_fNnYBoRGqfhWK4r7FUJo6BNu',
  'role': 'tool',
  'name': 'get_current_weather',
  'content': '{"location": "San Francisco", "temperature": "72", "unit": "fahrenheit"}'},
 {'tool_call_id': 'call_wzBuswuw0Wk47qleUmFCu2GZ',
  'role': 'tool',
  'name': 'get_current_weather',
  'content': '{"location": "Tokyo", "temperature": "10", "unit": "celsius"}'},
 {'tool_call_id': 'call_dU3wwhoDo7oVkSQyQIdJkyG6',
  'role': 'tool',
  'name': 'get_current_weather',
  'content': '{"location": "Paris", "temperature": "22", "unit": "celsius"}'
  }
]