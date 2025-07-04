from agents import (
    Runner,
    Agent,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    handoff,
    RunConfig,
    function_tool,
)
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


async def main():
    client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)
    config = RunConfig(tracing_disabled=True, model=model, model_provider=client)

    # Define tools for each agent
    @function_tool
    def calculate_refund(amount: float, reason: str) -> str:
        """Calculate refund amount and process it"""
        processing_fee = 2.50
        refund_amount = amount - processing_fee
        return f"Refund processed! Amount: ${refund_amount:.2f} (${processing_fee} processing fee deducted). Reason: {reason}"

    @function_tool
    def calculate_bill(amount: float, tax_rate: float = 0.08) -> str:
        """Calculate total bill with tax"""
        tax = amount * tax_rate
        total = amount + tax
        return f"Bill calculated: Subtotal: ${amount:.2f}, Tax: ${tax:.2f}, Total: ${total:.2f}"

    @function_tool
    def get_billing_info(customer_id: str) -> str:
        """Get customer billing information"""
        # Mock billing data
        mock_data = {
            "123": {
                "balance": 450.00,
                "last_payment": "2024-01-15",
                "status": "active",
            },
            "456": {"balance": 0.00, "last_payment": "2024-01-10", "status": "paid"},
        }
        info = mock_data.get(
            customer_id,
            {"balance": 125.00, "last_payment": "2024-01-01", "status": "pending"},
        )
        return f"Customer {customer_id} - Balance: ${info['balance']:.2f}, Last Payment: {info['last_payment']}, Status: {info['status']}"

    refund_agent = Agent(
        name="Refund Agent",
        instructions="""
        You are a refund specialist. Handle all refund-related requests professionally.

        Tasks you can do:
        1. Ask the user for the refund **amount** and **reason**.
        2. Use the `calculate_refund` tool to process the refund.
        3. Confirm refund clearly with deductions (like processing fee).
        4. If the user asks billing-related questions (account balance, bill calculation, or payment issues), use the billing agent handoff silently. Do not mention the transfer.
        5. Be empathetic, clear, and helpful in your responses.
        IMPORTANT: Do NOT mention transfers or handoffs to the user. Handle their requests seamlessly by using the billing agent's capabilities directly. The user should get their answer immediately without knowing about any transfers.
        """,
        model=model,
        tools=[calculate_refund],
    )

    billing_agent = Agent(
        name="Billing Agent",
        instructions="""You are a billing specialist. Handle all billing and payment-related questions professionally.

        Tasks you can do:
        1. Use the `calculate_bill` tool to calculate bills and tax.
        2. Use the `get_billing_info` tool to give account details.
        3. Handle payment issues or billing disputes.
        4. If the user asks for refunds or money returns, use the refund agent handoff silently. Do not mention the transfer.
        5. Be accurate, clear, and respectful in your tone.
        IMPORTANT: Do NOT mention transfers or handoffs to the user. Handle their requests seamlessly by using the refund agent's capabilities directly. The user should get their answer immediately without knowing about any transfers.""",
        model=model,
        tools=[calculate_bill, get_billing_info],
    )

    triage_agent = Agent(
        name="Customer Service Agent",
        instructions="""You are a customer service representative. Your job is to help customers with their inquiries.

        For billing questions, payment issues, or account inquiries -> use the billing agent handoff
        For refund requests or return issues -> use the refund agent handoff
        
        IMPORTANT: Do NOT mention transfers or handoffs to the user. Handle their requests seamlessly by using the appropriate agent's capabilities directly. The user should get their answer immediately without knowing about any transfers.""",
        model=model,
        handoffs=[handoff(billing_agent), handoff(refund_agent)],
    )

    print("Customer Service Bot Ready!")
    print("Try: 'I want a refund' or 'Check my bill' or 'What's my account balance?'")
    print("Type 'exit' to quit\n")

    history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Thank you for using our service!")
            break

        # Add user message to history
        history.append({"role": "user", "content": user_input})

        try:
            # Run the agent
            result = await Runner.run(triage_agent, history, run_config=config)

            # Add assistant response to history
            history.append({"role": "assistant", "content": result.final_output})

            print(f"Agent: {result.final_output}\n")

        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    asyncio.run(main())
