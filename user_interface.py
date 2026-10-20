import streamlit as st 
from llm_agent import ConversationAgent


class UserInterface:
	def __init__(self):
		st.set_page_config(page_title="Jarvis")
		st.title("Barbe-Quasar")
		self.conversation_agent_object = self.get_persistant_conversation_agent()


	def get_persistant_conversation_agent(self):
		
		if "conversation_agent_object" not in st.session_state:
			st.session_state.conversation_agent_object = ConversationAgent()

		return st.session_state.conversation_agent_object


	def show_discussion_history(self):
		for message in self.conversation_agent_object.get_conversation_history():
			with st.chat_message(message["role"]):
				st.markdown(message["content"])

	def audio_discussion (self):
		
		audio_value = st.audio_input("Record a voice message")
		
		if audio_value:
			st.audio(audio_value)
			transcribed_text = self.conversation_agent_object.transcribe_audio(audio_value)

			if transcribed_text:
				self.conversation_agent_object.ask_llm(transcribed_text)
				self.show_discussion_history()
	
	def run(self):
		text_interaction = st.chat_input(
			"Que veux tu moussaillon ?",
			accept_file=False,
			accept_audio=False,
			)

		if text_interaction :
			self.conversation_agent_object.ask_llm(text_interaction)
			self.show_discussion_history()

	


if __name__ == "__main__":
	user_interface_object = UserInterface()
	user_interface_object.run()
	user_interface_object.audio_discussion()








































	# response = ask_llm(user_input)
	# with st.chat_message("user"):
	# 	st.markdown(user_input)

	# with st.chat_message("system"):
	# 	st.markdown(response)


