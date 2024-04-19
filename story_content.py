story = {
    "start": {
        "text": "You're a young adventurer who has just entered the legendary Forest of Echoes, rumored to hold a powerful artifact. The path splits ahead of you.",
        "choices": [("Turn left towards the murky swamp", "swamp"), ("Go right into the dense forest", "forest")]
    },
    "swamp": {
        "text": "The swamp is thick and the air is filled with strange noises. Ahead, you see a glint of something shiny half-buried in the mud.",
        "choices": [("Investigate the shiny object", "shiny_object"), ("Continue through the swamp", "continue_swamp")]
    },
    "forest": {
        "text": "The forest is dark and full of towering trees. You hear a rustling sound from above.",
        "choices": [("Look up", "look_up"), ("Keep moving forward", "move_forward")]
    },
    "shiny_object": {
        "text": "You pull a bright, magical sword from the mud. It's the Sword of Light! Suddenly, a giant swamp creature emerges.",
        "choices": [("Use the sword to fight", "fight_creature"), ("Run away with the sword", "run_away")]
    },
    "continue_swamp": {
        "text": "You tread carefully through the swamp and eventually reach a peaceful clearing. You've safely navigated the swamp, but the artifact remains a mystery.",
        "choices": [("Head back to search again", "start"), ("Exit the forest", "peaceful_end")]
    },
    "look_up": {
        "text": "Above, a wise old owl perches, holding a golden key in its beak. It drops the key before flying away.",
        "choices": [("Pick up the key", "pick_key"), ("Continue without the key", "move_forward")]
    },
    "move_forward": {
        "text": "You continue deeper into the forest and stumble upon an ancient stone temple that's locked.",
        "choices": [("Try to find another way in", "find_another_way"), ("Leave the temple", "leave_temple")]
    },
    "fight_creature": {
        "text": "Armed with the Sword of Light, you bravely battle the swamp creature, driving it away. Victorious, you find that the creature was guarding an ancient chest filled with treasure.",
        "choices": [("Open the chest", "open_chest")]
    },
    "run_away": {
        "text": "You run as fast as you can, escaping the creature. Though you've survived, the forest's deeper secrets elude you as you exit with the magical sword.",
        "choices": [("Start over", "start"), ("Leave with the sword", "run_away_end")]
    },
    "pick_key": {
        "text": "With the golden key in hand, you approach the stone temple again.",
        "choices": [("Use the key on the temple door", "unlock_door"), ("Leave the key and temple", "leave_temple")]
    },
    "find_another_way": {
        "text": "As you circle the temple, you inadvertently trigger a trap and fall into a pit. You're stuck and must wait for rescue.",
        "choices": [("Wait for help", "wait_help")]
    },
    "leave_temple": {
        "text": "Deciding the temple's secrets aren't worth the risk, you leave the area. Your adventure ends, but the legend of the temple remains unsolved.",
        "choices": [("Return to start", "start"), ("Exit the forest", "peaceful_end")]
    },
    "open_chest": {
        "text": "Inside the chest, you find the Orb of Fate. With the orb and the sword, you now hold the power to alter destiny itself.",
        "choices": []
    },
    "unlock_door": {
        "text": "The key fits perfectly, and the temple door opens to reveal a room filled with ancient scrolls and artifacts.",
        "choices": [("Explore the room", "explore_room")]
    },
    "wait_help": {
        "text": "Hours pass before other adventurers find and rescue you. Though you're safe, the chance to uncover the temple's secrets is lost.",
        "choices": [("Return to start", "start")]
    },
    "explore_room": {
        "text": "As you explore, you discover a detailed map of the forest revealing its secrets, including a hidden escape route that leads to safety and fame.",
        "choices": []
    },
    "peaceful_end": {
        "text": "You've decided to leave the forest, taking with you the stories of your brief adventure. Maybe another day, another destiny awaits.",
        "choices": []
    },
    "run_away_end": {
        "text": "With the Sword of Light in your possession, you exit the forest, leaving its many mysteries unsolved. You're alive and have a powerful artifact, but the adventure feels incomplete.",
        "choices": []
    }
}
