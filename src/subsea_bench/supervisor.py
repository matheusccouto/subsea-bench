"""Supervisor LLM interface and implementations.

The Supervisor mediates all communication between the agent and the simulated
client (Devana Subsea).
It answers technical questions and reviews design submissions.
"""

from subsea_bench.models import ReviewVerdict, ReviewVerdictKind, SupervisorResponse


class Supervisor:
    """LLM-backed supervisor representing the Devana Subsea client."""

    async def answer_question(self, question: str, sim_day: float) -> SupervisorResponse:
        """Answer a technical question posed by the agent.

        Advances sim time and charges a question fee.
        """
        raise NotImplementedError

    async def review_submission(
        self,
        submission_text: str,
        round_number: int,
        sim_day: float,
    ) -> ReviewVerdict:
        """Review a design submission and return a verdict.

        Advances sim time and charges a review fee.
        """
        raise NotImplementedError


class LangChainSupervisor(Supervisor):
    """LangChain-backed supervisor using a retriever and chat model.

    Retriever grounds answers in project facts; the chat model produces
    natural human-sounding replies on behalf of Devana Subsea.
    Vector-store choice is deferred until the first scenario needs indexing.
    """

    def __init__(self, retriever: object, chat_model: object) -> None:
        """Store the retriever and chat model for use when implemented."""
        self._retriever = retriever
        self._chat_model = chat_model

    async def answer_question(self, question: str, sim_day: float) -> SupervisorResponse:
        """Answer using retrieved project facts rendered through the chat model."""
        raise NotImplementedError

    async def review_submission(
        self,
        submission_text: str,
        round_number: int,
        sim_day: float,
    ) -> ReviewVerdict:
        """Review the submission against retrieved scope documents."""
        raise NotImplementedError


class FakeSupervisor(Supervisor):
    """Deterministic stub supervisor for unit tests.

    Returns canned responses without calling any LLM.
    """

    def __init__(
        self,
        answer: str = "Yes.",
        verdict_kind: ReviewVerdictKind = ReviewVerdictKind.APPROVED,
        verdict_comments: str = "Looks good.",
    ) -> None:
        """Store canned responses to return from both methods."""
        self._answer = answer
        self._verdict_kind = verdict_kind
        self._verdict_comments = verdict_comments

    async def answer_question(self, question: str, sim_day: float) -> SupervisorResponse:
        """Return the canned answer regardless of the question."""
        raise NotImplementedError

    async def review_submission(
        self,
        submission_text: str,
        round_number: int,
        sim_day: float,
    ) -> ReviewVerdict:
        """Return the canned verdict regardless of the submission."""
        raise NotImplementedError
