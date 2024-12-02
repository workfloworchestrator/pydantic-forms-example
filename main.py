from dataclasses import dataclass
from typing import Annotated, Iterator
from annotated_types import SLOTS, BaseMetadata, GroupedMetadata
from fastapi import FastAPI
from pydantic import ConfigDict, Field
from pydantic_forms.core import FormPage, generate_form
from pydantic_forms.types import State

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@dataclass(frozen=True, **SLOTS)
class ExtraData(GroupedMetadata):
    props: dict

    def __iter__(self) -> Iterator[BaseMetadata]:
        yield Field(json_schema_extra=self.props)


@app.get("/form")
async def form():
    def form_generator(state: State):
        class TestForm(FormPage):
            model_config = ConfigDict(title="Form Title")

            test: str
            input: Annotated[str, ExtraData(props={"prop1": "val", "prop2": "val"})]

        yield TestForm

    return generate_form(form_generator, state={}, user_inputs=[])


