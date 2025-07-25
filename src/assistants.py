# src/assistants.py
import os
from datetime import datetime

from dotenv import load_dotenv
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

from .prompts import sales_rep_prompt, support_prompt
from .state import State
from .tools import (
    DEFAULT_USER_ID,
    EscalateToHuman,
    RouteToCustomerSupport,
    cart_tool,
    search_tool,
    set_thread_id,
    set_user_id,
    structured_search_tool,
    view_cart,
)

load_dotenv()
import pandas as pd

# Setup LLM
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY") or "Empty"
llm = ChatOpenAI(api_key=OPENAI_API_KEY)

# Tool registration
sales_tools = [
    tool(RouteToCustomerSupport),
    search_tool,
    structured_search_tool,
    cart_tool,
    view_cart,
]
support_tools = [EscalateToHuman]

# Runnable pipelines
sales_runnable = sales_rep_prompt.partial(time=datetime.now) | llm.bind_tools(
    sales_tools
)
support_runnable = support_prompt.partial(time=datetime.now) | llm.bind_tools(
    support_tools
)

# TODO
def sales_assistant(state: State, config: RunnableConfig, runnable=sales_runnable) -> dict:
    """
    LangGraph node function for running the sales assistant LLM agent.

    This function binds a chat prompt (`sales_rep_prompt`) with tools and invokes
    the LangChain Runnable pipeline. It sets the thread and user IDs and runs the
    agent with the given state and config.

    ---
    Arguments:
    - state (State): LangGraph state with current dialog history.
    - config (RunnableConfig): Config object that contains the `thread_id`.
    - runnable: (optional) The runnable to use; defaults to global `sales_runnable`.

    ---
    Behavior:
    - Extract thread ID from config and set it using `set_thread_id(...)`.
    - Set default user ID via `set_user_id(...)`.
    - Use the given `runnable` to run the assistant logic.

    ---
    Returns:
    - A dictionary with a `"messages"` key containing the new AI message(s).
    Example: `{"messages": [AIMessage(...)]}`
    """
    # Extrae el thread_id del config y lo guarda
    set_thread_id(config["configurable"]["thread_id"]) #  Asocia una sesión de conversación (como si fuera un chat individual).
    
    # Asigna un user_id por defecto para simular un usuario
    set_user_id(DEFAULT_USER_ID) #Asocia un usuario por defecto para que el sistema sepa sobre qué historial operar.
    
    # Ejecuta el pipeline con el estado y configuración
    return {"messages": runnable.invoke(state, config=config)} # Llama al agente LLM con las herramientas y el prompt de ventas (sales_rep_prompt) para generar la siguiente respuesta en la conversación.
                 #Esto es necesario para que el grafo de conversación sepa cómo manejar la interacción con el asistente de ventas

def support_assistant(state: State, config: RunnableConfig) -> dict:
    set_thread_id(config["configurable"]["thread_id"])
    return {"messages": support_runnable.invoke(state, config=config)}
