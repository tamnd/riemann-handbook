---
id: local-global-compat-at-iwahori-fixed-of-unlinked
title: Local-global compatibility at depth zero, from the unlinked case
kind: theorem
decl: UpperTheory.Gal.ToralGalois.R2.localGlobalCompatAtIwahoriFixed_of_unlinked
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.SphericalGaloisCompatibility.PAdicSplitting.LocalGlobalCompatAtIwahoriFixedOfUnlinked
covers: 1522
status: drafted
drafted_by: writer@claude
---
This theorem extends local-global compatibility from places where the local component has an unlinked support of characters (the statement `R1`) to places of depth zero. It is the second input of [the Galois row from the spherical core](/entry/rest/). The proof reduces the new case to `R1` by a base change, given by [toTor_holds](/entry/to-tor-holds/). Below this theorem are 1,522 declarations, and 1,506 of them are below `toTor_holds`.

## Statement

Let $E$ be a CM field, $\ell$ a prime with $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$, $n \geq 1$, and $\pi$ a regular algebraic cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_E)$ in a polarized pair. Let $r \colon G_E \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ be attached to $\pi$ (`Weak`). Let $w$ be a finite place and $\sigma = \pi_w$. Put $\sigma^\circ = \sigma \otimes |\det|^{(1-n)/2}$.

Suppose:

1. $\sigma$ has a nonzero vector fixed by $K_1 = \ker(\mathrm{GL}_n(\mathcal{O}_w) \to \mathrm{GL}_n(k_w))$;
2. either the cuspidal support of $\sigma^\circ$ consists of characters, no two linked by $|\cdot|$, or $E_w \cong \mathbb{Q}_g$ for a prime $g$ and the members of size at least 2 of each cuspidal support of $\sigma^\circ$ are pairwise not unramified twists of each other;
3. $\mathrm{rec}$ is a local Langlands map with [IsRecT](/step/is-rect-def/), and $\mathrm{rec}(\sigma^\circ)$ has monodromy $N = 0$.

Then, for $w \nmid \ell$, the Weil-Deligne class of $r$ at $w$ has $N = 0$, and each element of inertia has the same characteristic polynomial on it as on $\mathrm{rec}(\sigma^\circ)$. For $w \mid \ell$, $r$ is de Rham at $w$ with the expected Hodge-Tate jumps, it is potentially semistable (`IsPstAt`), and the same two facts hold for its Weil-Deligne class `wdAt`.

**Theorem.** `R1` implies this statement.

## Proof

If the support is of characters and unlinked, `R1` applies directly. Otherwise:

1. `mixedOf` shows that $\sigma$ is *mixed*: it has depth zero and an unlinked support whose members of size at least 2 are pairwise not unramified twists.
2. [toTor_holds](/entry/to-tor-holds/) gives an abelian CM extension $K/E$, a cuspidal $P$ on $\mathrm{GL}_n(\mathbb{A}_K)$ attached to $r|_{G_K}$, and a component $T = P_u$ above $w$ whose support is of unlinked characters, with the same inertia characteristic polynomials as $\sigma^\circ$.
3. `R1` over $K$ gives the result for $r|_{G_K}$ at $u$. The lemmas `wdOf_restricts` and `restricts_lpDim_mono0_charPol` bring it back to $w$ away from $\ell$. Above $\ell$, `drDesc` (de Rham descends from $K$), `isPstAt_of_resTo` and `wdAt_resTo` do the same.

## In the Lean code

The theorem is in [LocalGlobalCompatAtIwahoriFixedOfUnlinked.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/PAdicSplitting/LocalGlobalCompatAtIwahoriFixedOfUnlinked.lean#L18). The proof is `r2g mixedOf toTor_holds drDesc recTExists`. The case split is in `r2g`, in [R2g.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/PAdicSplitting/R2g.lean#L14). The statement is in [LocalGlobalCompatAtIwahoriFixedPlaces.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/PAdicSplitting/LocalGlobalCompatAtIwahoriFixedPlaces.lean#L16). We have not unfolded `wdOf`, `wdAt` and `IsPstAt`.

Two points differ from what the name says. The hypothesis is a vector fixed by $K_1$, not by an Iwahori subgroup. Since $K_1$ is in the Iwahori subgroup, this is a weaker hypothesis. And $N = 0$ for $\mathrm{rec}(\sigma^\circ)$ is a hypothesis: the theorem carries $N = 0$ from $\mathrm{rec}(\sigma^\circ)$ to $r$, and does not prove it.
