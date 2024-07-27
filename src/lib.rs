use yew::prelude::*;
use serde::{Deserialize, Serialize};
use wasm_bindgen::prelude::*;
use anyhow::Result;
use wasm_bindgen_futures::spawn_local;
use web_sys::HtmlInputElement;
use std::rc::Rc;
use aptos_sdk::{
    rest_client::Client,
    types::account_address::AccountAddress,
};

#[derive(Serialize, Deserialize, Clone, PartialEq)]
pub struct UserProfile {
    id: u64,
    name: String,
    skills: Vec<String>,
}

#[function_component(App)]
pub fn app() -> Html {
    let user_profile = use_state(|| UserProfile {
        id: 1,
        name: String::new(),
        skills: Vec::new(),
    });

    let name_ref = use_node_ref();
    let skill_ref = use_node_ref();

    let on_name_change = {
        let user_profile = user_profile.clone();
        Callback::from(move |e: Event| {
            let input: HtmlInputElement = e.target_unchecked_into();
            user_profile.set(UserProfile {
                name: input.value(),
                ..(*user_profile).clone()
            });
        })
    };

    let add_skill = {
        let user_profile = user_profile.clone();
        let skill_ref = skill_ref.clone();
        Callback::from(move |_| {
            let skill_input = skill_ref.cast::<HtmlInputElement>().unwrap();
            let mut updated_profile = (*user_profile).clone();
            updated_profile.skills.push(skill_input.value());
            user_profile.set(updated_profile);
            skill_input.set_value("");
        })
    };

    let create_profile = {
        let user_profile = Rc::new((*user_profile).clone());
        Callback::from(move |_| {
            let user_profile = user_profile.clone();
            spawn_local(async move {
                if let Err(e) = create_user_profile_on_aptos((*user_profile).clone()).await {
                    log::error!("Error creating user profile: {:?}", e);
                }
            });
        })
    };

    html! {
        <div>
            <h1>{ "YOPEX - Decentralized Talent Acquisition" }</h1>
            <input
                ref={name_ref}
                type="text"
                placeholder="Your Name"
                onchange={on_name_change}
            />
            <input
                ref={skill_ref}
                type="text"
                placeholder="Add a Skill"
            />
            <button onclick={add_skill}>{ "Add Skill" }</button>
            <button onclick={create_profile}>{ "Create Profile on Aptos" }</button>
            <div>
                <h2>{ "Your Profile" }</h2>
                <p>{ format!("Name: {}", user_profile.name) }</p>
                <p>{ "Skills:" }</p>
                <ul>
                    { for user_profile.skills.iter().map(|skill| html! { <li>{ skill }</li> }) }
                </ul>
            </div>
        </div>
    }
}

async fn create_user_profile_on_aptos(user_profile: UserProfile) -> Result<()> {
    let client = Client::new("https://fullnode.devnet.aptoslabs.com".to_string());

    // Placeholder: Replace with actual account address handling
    let account = AccountAddress::from_hex_literal("0x1")?;

    log::info!("Simulating creation of user profile on Aptos for account: {:?}", account);
    log::info!("User Profile: {:?}", user_profile);

    // In a real implementation, you would create, sign, and submit a transaction here

    Ok(())
}

#[wasm_bindgen]
pub fn run_app() -> Result<(), JsValue> {
    yew::Renderer::<App>::new().render();
    Ok(())
}