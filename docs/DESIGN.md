# Design System Document

## 1. Overview & Creative North Star: "Kinetic Brutalism"

This design system is engineered to capture the raw, unyielding energy of a high-intensity CrossFit environment. Our Creative North Star is **"Kinetic Brutalism."** Unlike standard corporate "modern" designs that favor soft safety, this system embraces high-contrast tension, industrial grit, and architectural weight. 

We break the "template" look through:
*   **Intentional Asymmetry:** Utilizing staggered layouts and overlapping typography to mimic the movement and controlled chaos of a workout.
*   **Scale Distortion:** Massive display type juxtaposed with utility-focused labels to create a sense of dominance and authority.
*   **Tonal Depth:** Moving away from flat black to a sophisticated charcoal hierarchy that feels premium and "expensive," not just dark.

## 2. Colors

The palette is a high-tension triad of Power Red, Crisp White, and Deep Charcoal.

### Palette Strategy
*   **Primary (#D2261E):** Used strictly for "Action" and "Urgency." It is our energetic catalyst. Use it for CTAs, highlights, and critical data points.
*   **Surface Hierarchy (The Charcoal Spectrum):** 
    *   `surface` (#131313): The canvas.
    *   `surface-container-low` (#1C1B1B): For secondary sectioning.
    *   `surface-container-highest` (#353534): For elevated interactive elements.
*   **On-Surface (#E5E2E1):** Not a pure white, but a "Crisp Bone" to reduce eye strain while maintaining maximum contrast against the dark background.

### The "No-Line" Rule
**Explicit Instruction:** Prohibit the use of 1px solid borders for sectioning or containment. Boundaries must be defined solely through background color shifts. For example, a workout schedule block (`surface-container-low`) should sit on the main page background (`surface`) to define its edge. 

### The "Glass & Gradient" Rule
To elevate the aesthetic from "gritty" to "premium," use Glassmorphism for floating overlays (e.g., sticky navbars or modal cards). Use `surface-container-highest` at 60% opacity with a `20px` backdrop-blur. 
*   **Signature Texture:** Use a subtle linear gradient on primary CTAs transitioning from `primary_container` (#D2261E) to `on_primary_fixed_variant` (#930004) at a 135-degree angle. This adds "soul" and a metallic, automotive sheen.

## 3. Typography

The typography is the backbone of the brand's "Athletic Modern" persona.

*   **Display (Space Grotesk):** Our "Voice of Power." Use `display-lg` (3.5rem) with tight letter-spacing (-0.04em) for hero headlines. It should feel massive, almost architectural.
*   **Headlines (Space Grotesk):** Used for section titles. These should frequently utilize *Uppercase* styling to reinforce the "Kinetic Brutalism" vibe.
*   **Body (Inter):** Our "Voice of Precision." Inter provides the technical, modern readability required for training programs and class descriptions.
*   **Labels (Space Grotesk):** Small, all-caps utility text. These act as "technical callouts" in the UI, similar to the branding on gym equipment.

## 4. Elevation & Depth

We eschew traditional drop shadows for **Tonal Layering.**

*   **The Layering Principle:** Stacking tiers creates natural lift. Place a `surface-container-lowest` (#0E0E0E) card inside a `surface-container-low` (#1C1B1B) section to create a recessed, "carved-out" look. 
*   **Ambient Shadows:** If a floating element (like a "Join Now" button) requires a shadow, it must be extra-diffused. 
    *   *Blur:* 32px | *Opacity:* 15% | *Color:* Primary Red (#D2261E) — this creates a "red glow" rather than a grey shadow, suggesting energy emission.
*   **The "Ghost Border" Fallback:** If a boundary is strictly required for accessibility, use the `outline-variant` (#5C403C) at **15% opacity**. Never use 100% opaque lines.

## 5. Components

### Buttons
*   **Primary:** Sharp corners (`none` or `sm` roundedness). Background: Signature Red Gradient. Text: White, Bold, All-Caps.
*   **Secondary:** `surface-container-highest` background with a `Ghost Border`.
*   **Interaction:** On hover, primary buttons should "glow" (increase shadow spread), never shift color significantly.

### Cards & Lists
*   **The Divider Ban:** Forbid the use of divider lines in lists. Instead, use `3.5rem` (Spacing 10) of vertical white space or alternating background shifts between `surface-container-low` and `surface-container-highest`.
*   **Impact Imagery:** Cards should feature full-bleed imagery with a `surface_container_lowest` gradient overlay on the bottom 40% to house white text.

### Input Fields
*   **Style:** Minimalist. No background fill, only a bottom "Ghost Border." 
*   **Active State:** The bottom border transforms into a 2px `primary` red line.

### Athletic Chips
*   **Context:** Used for class difficulty (e.g., "Beginner," "Elite").
*   **Style:** `surface-container-highest` background, `label-sm` typography, and a `1.5` spacing padding.

## 6. Do's and Don'ts

### Do
*   **DO** use large-scale imagery of chalk, sweat, and iron.
*   **DO** overlap typography over images to create depth.
*   **DO** use the `primary` red sparingly to ensure it maintains its "High-Energy" impact.
*   **DO** keep corners sharp (0px) or slightly softened (0.25rem) to maintain an aggressive profile.

### Don't
*   **DON'T** use rounded "pill" buttons; it dilutes the gritty, athletic authority of the brand.
*   **DON'T** use traditional 1px grey borders; it makes the site look like a template.
*   **DON'T** use soft pastels or any colors outside the defined palette.
*   **DON'T** center-align everything. Use the grid to create "Heavy" left-aligned blocks that feel grounded.