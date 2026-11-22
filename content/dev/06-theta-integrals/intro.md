---
title: Introduction
---
This volume gives the parts below [the chapter on theta integrals and local matching](/proof/theta-matching/). That chapter has two branches. The first gives the two theta statements `ThetaIntegralsAgree` and `LocalMatching` on unitary groups, which [the trunk step](/step/theta-local-matching/) needs. The second is a short branch, [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/), that ends in the nonvanishing of $L(s, \psi)$ for $\operatorname{Re}(s) > \tfrac12$. The chapter and its steps explain the top of each branch. This volume gives the parts below them, one declaration in each entry.

The two branches have 20,590 declarations. The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Theta pair lifts.** The top of the second branch. [`shape_closed_link_n_of_green`](/entry/shape-closed-link-n-of-green/) turns the statement [Green](/step/green-def/) into an implication whose conclusion is the statement `TopG`. Then two of its inputs: the valuation bound `adm2`, and the service bound `ServF`.
- **Group lattices.** The bound `LinkG`, another input of the same implication, and the local statement `Loc` that it needs.
- **Growth bounds.** Statement E, the closed form of a numerical bound on a family of data, through a chain of reductions to the bound `RestMEM`.
- **Sharp restriction.** The bound `ServF` from a sum over primes.
- **Automorphic arithmetic.** The only place where the window bound [VWin](/step/vwin-def/) enters the second branch: hosts on windows of scale $\tfrac32$ for each primitive character.
- **Weil bound.** The first branch. [`theoremK_head2`](/entry/theorem-k-head2/) gets the two theta statements from the continuation of Siegel Eisenstein series and the Siegel-Weil formula, and [`closeSph`](/entry/close-sph/) assembles them from fourteen local and global inputs. Then the Siegel-Weil formula from the constant term split.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. In this volume many theorems only pass hypotheses along, and several take hypotheses that they never use. The entry says so and points to the theorem with the content.
