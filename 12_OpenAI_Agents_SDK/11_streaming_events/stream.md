There are three types of stream events:

* RawResponsesStreamEvent
* RunItemStreamEvent
* AgentUpdatedStreamEvent



***RawResponsesStreamEvent:***
Streaming event from the LLM. These are 'raw' events, i.e. they are directly passed through from the LLM.

(RunItemStreamEvent.type)

The raw responses streaming event from the LLM.
type: Literal['raw_response_event'] = 'raw_response_event'



***RunItemStreamEvent:***
Streaming events that wrap a RunItem. As the agent processes the LLM response, it will generate these events for new messages, tool calls, tool outputs, handoffs, etc.

There are different kinds of events(RunItemStreamEvent.name):

- message_output_created
- handoff_requested
- handoff_occured
- tool_called
- tool_output
- reasoning_item_created
- mcp_approval_requested
- mcp_approval_response
- mcp_list_tools


***AgentUpdatedStreamEvent:***
Event that notifies that there is a new agent running. `First` event when agent loop runs i.e new agent start running

new_agent: Agent[Any]



