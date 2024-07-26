use yew::prelude::*;
use serde::{Deserialize, Serialize};
use wasm_bindgen::prelude::*;
use anyhow::Result;
use wasm_bindgen_futures::spawn_local;
use web_sys::HtmlInputElement;
use std::rc::Rc;

#[derive(Serialize, Deserialize, Clone, PartialEq)]
struct Project {
    id: u64,
    name: String,
    description: String,
}

#[function_component(App)]
fn app() -> Html {
    let project = use_state(|| Project {
        id: 1,
        name: String::new(),
        description: String::new(),
    });

    let name_ref = use_node_ref();
    let description_ref = use_node_ref();

    let on_name_change = {
        let project = project.clone();
        Callback::from(move |e: Event| {
            let input: HtmlInputElement = e.target_unchecked_into();
            project.set(Project {
                name: input.value(),
                ..(*project).clone()
            });
        })
    };

    let on_description_change = {
        let project = project.clone();
        Callback::from(move |e: Event| {
            let input: HtmlInputElement = e.target_unchecked_into();
            project.set(Project {
                description: input.value(),
                ..(*project).clone()
            });
        })
    };

    let create_nft = {
        let project = Rc::new((*project).clone());
        Callback::from(move |_| {
            let project = project.clone();
            spawn_local(async move {
                if let Err(e) = create_nft((*project).clone()).await {
                    log::error!("Error creating NFT: {:?}", e);
                }
            });
        })
    };

    html! {
        <div>
            <h1>{ "Aptos NFT Project" }</h1>
            <input
                ref={name_ref}
                type="text"
                placeholder="Project Name"
                onchange={on_name_change}
            />
            <input
                ref={description_ref}
                type="text"
                placeholder="Project Description"
                onchange={on_description_change}
            />
            <button onclick={create_nft}>{ "Create NFT" }</button>
            <p>{ format!("Current Project: {} - {}", project.name, project.description) }</p>
        </div>
    }
}

async fn create_nft(project: Project) -> Result<()> {
    let client = reqwest::Client::new();
    let res = client.post("http://localhost:8080/create_nft")
        .json(&project)
        .send()
        .await?;
    if res.status().is_success() {
        log::info!("NFT created successfully!");
    } else {
        log::error!("Failed to create NFT");
    }
    Ok(())
}

#[wasm_bindgen]
pub fn run_app() -> Result<(), JsValue> {
    yew::Renderer::<App>::new().render();
    Ok(())
}