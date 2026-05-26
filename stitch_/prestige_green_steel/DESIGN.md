---
name: Prestige Green & Steel
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#414941'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#717970'
  outline-variant: '#c1c9be'
  surface-tint: '#396841'
  primary: '#0c3d1b'
  on-primary: '#ffffff'
  primary-container: '#265530'
  on-primary-container: '#95c899'
  inverse-primary: '#9fd3a3'
  secondary: '#775a19'
  on-secondary: '#ffffff'
  secondary-container: '#fed488'
  on-secondary-container: '#785a1a'
  tertiary: '#353534'
  on-tertiary: '#ffffff'
  tertiary-container: '#4c4b4b'
  on-tertiary-container: '#bdbbbb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bbf0be'
  primary-fixed-dim: '#9fd3a3'
  on-primary-fixed: '#002109'
  on-primary-fixed-variant: '#21502c'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e9c176'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4201'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
---

## Brand & Style

The brand personality for the design system is defined by a sophisticated, elite social club aesthetic tailored for a modern Hold'em pub franchise. It targets an audience that values professionalism, fair play, and a premium lifestyle experience. The UI evokes a sense of trust and exclusivity through a "Corporate Modern" approach—balancing the excitement of gaming with the refined atmosphere of a high-end lounge.

The style leverages **Minimalism** to ensure the interface feels uncluttered and high-end. Expect heavy use of whitespace to let the Deep Green brand color act as a focal point of prestige. Lines are thin and precise, and the overall composition follows a strict mathematical rhythm to reinforce the "trustworthy" brand pillar.

## Colors

The palette is anchored by a **Deep Green** primary color, synonymous with the heritage of card games and high-stakes tables, but rendered in a forest-toned hex to maintain a premium feel. 

- **Primary (#265530):** Used for key actions, brand identity, and hero sections.
- **Secondary (#C5A059):** A muted gold used sparingly for accents, "VIP" status indicators, or highlights to reinforce the sophisticated theme.
- **Background:** Pure white (#FFFFFF) is the foundation to provide a clean, modern contrast against the dark green.
- **Text:** Primary headings use a near-black (#1A1A1A) for maximum legibility. Sub-text uses a neutral light gray (#757575) to establish visual hierarchy without cluttering the view.

## Typography

This design system utilizes **Hanken Grotesk** for headlines to provide a sharp, contemporary, and professional edge. Its geometric clarity aligns with the "trustworthy" brand value. For body copy and functional UI elements, **Inter** is employed due to its exceptional legibility and systematic nature.

Hierarchy is strictly enforced. Large headlines use tighter letter spacing and bold weights to command attention, while labels use all-caps and increased tracking for a refined, editorial feel. All Korean text should map to these weights and sizes using local system fallbacks that match the Sans-serif structure.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to maintain a contained, premium feel reminiscent of a curated editorial spread. A 12-column grid is used with generous gutters to ensure "breathing room."

- **Desktop:** 1200px max-width container, centered.
- **Tablet:** 8-column fluid grid with 24px margins.
- **Mobile:** 4-column fluid grid with 16px margins.

Spacing follows an 8px base unit. Vertical rhythm is emphasized to separate content sections clearly, using the 'lg' (48px) and 'xl' (80px) tokens to create the requested "generous whitespace."

## Elevation & Depth

To maintain a "Professional and Sophisticated" look, the design system avoids heavy shadows or neomorphism. Instead, it uses **Low-contrast outlines** and **Tonal layers**.

- **Surfaces:** Secondary content is placed on very light gray backgrounds or within containers with a subtle 1px border (#E0E0E0).
- **Depth:** When elevation is required (e.g., for modals or dropdowns), a single, ultra-diffused ambient shadow is used: `0px 10px 30px rgba(0, 0, 0, 0.05)`.
- **Interactions:** Hover states should shift the background color slightly or deepen the border weight rather than increasing shadow depth, keeping the UI flat and architectural.

## Shapes

The shape language is "Soft" (0.25rem / 4px). This subtle rounding takes the aggressive edge off the "Brutalist" sharp corners while remaining significantly more professional and serious than "Rounded" or "Pill" styles. 

- **Buttons & Inputs:** Use the standard 4px radius.
- **Cards:** May use a slightly larger 8px (rounded-lg) radius to create a container-like feel.
- **Selection Indicators:** Use sharp 0px or soft 2px radii for a precise, technical look.

## Components

### Buttons
- **Primary:** Solid Deep Green (#265530) with White text. Bold weight, 4px corner radius.
- **Secondary:** Transparent background with a 1px Deep Green border. 
- **Tertiary:** Pure text buttons in Deep Green with an underline on hover.

### Input Fields
- **Style:** Outlined with a 1px light gray border. On focus, the border transitions to Deep Green.
- **Labels:** Use the `label-caps` typography style, positioned above the field.

### Cards
- **Structure:** White background, 1px light gray border, 8px corner radius. No shadow by default.
- **Usage:** Used for game types, pub location details, and event listings.

### Chips & Badges
- **Status Badges:** Small, all-caps text. Use Deep Green for "Active" and a muted Gold for "Premium/VIP."

### Lists
- **Style:** Clean dividers (1px, light gray) with generous padding (16px top/bottom) between items. Icons should be monochrome and minimal.

### Navigation
- **Top Bar:** Fixed, pure white background, minimal Deep Green logo on the left, with navigation links in Primary Text (#1A1A1A). Items have a 2px Green bottom border on active/hover states.