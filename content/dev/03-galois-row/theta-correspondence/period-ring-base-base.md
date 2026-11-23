---
id: period-ring-base-base
title: The basic properties of the crystalline period ring
kind: theorem
decl: period_ring_base.base
module: Development.AutomorphicArithmetic.ThetaCorrespondence.FockModels.TiltedDrinfeld.Base
covers: 315
status: drafted
drafted_by: writer@claude
---
This theorem collects 40 facts about the period rings $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$ of $\mathbb{Q}_\ell$ into one structure. It has no argument of its own: each field is a separate lemma. Nine declarations use it directly, for example in the $p$-adic comparison files `CrisSurj.lean` and `SmoothQ.lean`. All of them lie below [the local steps](/entry/steps-holds/), which is the closest entry above it.

## Statement

For each prime $\ell$, `Base ℓ` holds. Let $G = \mathrm{Gal}(\overline{\mathbb{Q}}_\ell / \mathbb{Q}_\ell)$, $B$ the Lean `Bcris ℓ` with Frobenius $\varphi$ and map $\iota \colon B \to B_{\mathrm{dR}}$, $t$ the period of the cyclotomic character $\chi$, and $\theta \colon B_{\mathrm{dR}}^+ \to \mathbb{C}_\ell$. The fields of `Base`, in groups:

- **Actions.** $G$ acts on $B$, $B_{\mathrm{dR}}$ and $\mathbb{C}_\ell$; $\varphi$ and $\iota$ commute with it; $\mathbb{Q}_\ell$ is fixed. $B$ is a domain and $\iota$ is injective.
- **The period $t$.** $t$ is a unit of $B$, $\varphi(t) = \ell t$, $g(t) = \chi(g) t$, and $\iota(t)$ is the period $t$ of $B_{\mathrm{dR}}$. An element $u$ of $B_{\mathrm{st}}$ has $g(u) = u + \kappa(g) t$, with $\kappa$ a continuous Kummer cocycle.
- **$B_{\mathrm{dR}}$.** $\theta$ is a $G$-equivariant ring map on $B_{\mathrm{dR}}^+$ with kernel $t B_{\mathrm{dR}}^+$, and each nonzero $x$ is $t^i$ times a unit of $B_{\mathrm{dR}}^+$.
- **The fundamental sequence.** If $\varphi(x) = x$ and $\iota(x) \in B_{\mathrm{dR}}^+$, then $x \in \mathbb{Q}_\ell$; and $B^{\varphi = 1} \to B_{\mathrm{dR}} / B_{\mathrm{dR}}^+$ is onto (`fs_ker`, `fs_surj`). This is the fundamental exact sequence of Fontaine (Le corps des périodes $p$-adiques, Astérisque 223, 1994).
- **Fixed points.** For a finite extension $L$, the $G_L$-invariants of $B$ are spanned over $\mathbb{Q}_\ell$ by finitely many invariant elements of the image of $A_{\mathrm{inf}}[1/\ell]$ (`fixed`). No $x \in B$ has $g(x) - x = \kappa(g) t$ for all $g \in G_L$ (`no_kummer`).
- **$A_{\mathrm{inf}}$.** The image of $A_{\mathrm{inf}}[1/\ell]$ in $B$ is stable under $\varphi$ and $G$, lands in $B_{\mathrm{dR}}^+$, and has no nonzero $x$ with $\varphi^h(x) = \ell^m x$ for $m \neq 0$.

## Proof

The proof fills each field with one lemma, most named `base_` and the field, such as `base_fs_ker` and `base_no_kummer`. The fundamental sequence comes from `PositivityTheory.LocInh.fund` and `fund_onto`; `fixed` uses the maximal unramified subextension of $L$; `no_kummer` uses `GlobalTheory.MemLoc.exists_locPrime_tied`, `UpperTheory.Lit.Drps.exists_beta` and `GlobalTheory.Pst.StLat.kummer_not_frac`. We have not unfolded these.

## In the Lean code

The theorem is in [Base.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/FockModels/TiltedDrinfeld/Base.lean#L11). The structure `Base` and `PeriodRingBase` are in [DieudonneManinBasisModification.lean](lean:Development/WeilBound/RepresentationTheoryGL/PeriodRingBases/PeriodRingUnits/DieudonneManinBasisModification.lean#L84). The module path says "Fock models" and "tilted Drinfeld", and the structure sits in a file named for Dieudonné-Manin bases, but the statement is about period rings only.
