---
id: to-tor-holds
title: A mixed depth-zero component becomes a torus component after base change
kind: theorem
decl: UpperTheory.Gal.ToralGalois.R2.toTor_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.SphericalGaloisCompatibility.PAdicSplitting.LocalGlobalCompatAtIwahoriFixedOfUnlinked
covers: 1506
status: drafted
drafted_by: writer@claude
---
This theorem proves `ToTor`, the base change step of [local-global compatibility at depth zero](/entry/local-global-compat-at-iwahori-fixed-of-unlinked/). It turns a mixed local component at a place with completion $\mathbb{Q}_g$ into a component whose support is of unlinked characters, so that `R1` applies. The proof only passes seven proved facts to the lemma `toTor`. The main input is [suppBC_outright](/entry/supp-bc-outright/) (1,313 of the 1,506 declarations below this theorem).

## Statement

Let $E$, $\ell$, $\iota$, $n$, $\pi$, $\chi$ and $r$ be as in [the entry above](/entry/local-global-compat-at-iwahori-fixed-of-unlinked/). Let $w$ be a place of $E$ with $E_w \cong \mathbb{Q}_g$, and let $\sigma = \pi_w$ be *mixed*: it has a nonzero $K_1$-fixed vector and a cuspidal support with no two members linked by $|\cdot|$, whose members of size at least 2 are pairwise not unramified twists. Let $A$ be a valuation ring over $w$ and $\mathrm{rec}$ a map with [IsRecT](/step/is-rect-def/).

**Theorem.** There are an abelian Galois CM extension $K/E$, a place $u$ of $K$ under $A$, and a cuspidal $P$ on $\mathrm{GL}_n(\mathbb{A}_K)$ with a character $\chi'$, such that:

1. $(P, \chi')$ is in scope, and $r|_{G_K}$ is attached to $P$;
2. $P$ and $\pi$ have the same infinitesimal characters, through $E \to K$;
3. $T = P_u$ has a support of characters with no two linked, after the twist by $|\det|^{(1-n)/2}$;
4. there is a map $\mathrm{rec}'$ with `IsRecT` at $u$ such that each element $t$ of inertia over $E$ is an element $t'$ of inertia over $K$, and $t'$ on $\mathrm{rec}'(T^\circ)$ has the same characteristic polynomial as $t$ on $\mathrm{rec}(\sigma^\circ)$.

## Proof

The lemma `toTor` takes seven facts and gives `ToTor`. Its proof runs as follows.

1. Since $E_w \cong \mathbb{Q}_g$, the place $w$ is split (`IsSplitAt`) with norm $g$ (`split_of_padic`).
2. `unrField_holds` (105 declarations) gives an abelian CM extension $K/E$ in which inertia at $w$ and at the non-split places acts trivially, and each place over $w$ has norm $g^{n!}$.
3. `NearKilling.allLift_holds` (48) gives $P$ on $\mathrm{GL}_n(\mathbb{A}_K)$, reached from $\pi$ by a chain of cyclic base changes, in scope, with $r|_{G_K}$ attached to it.
4. `ineNorm` identifies the inertia groups over $E$ and $K$, compatibly with the local Artin maps through the norm.
5. `suppBC_outright` gives tame characters $\xi_1, \dots, \xi_n$ that form the support of $T$, with no two linked since $\sigma$ is mixed, and the inertia polynomials of $\mathrm{rec}(\sigma)$ in terms of the $\xi_j$.
6. `recTExists` gives $\mathrm{rec}'$, and `recChars` computes the inertia polynomials of $\mathrm{rec}'(T^\circ)$ from the $\xi_j$. `infLifts` gives clause 2.

So the content is in [suppBC_outright](/entry/supp-bc-outright/). We have not unfolded `Tower` in `UnrField`.

## In the Lean code

The theorem is in [LocalGlobalCompatAtIwahoriFixedOfUnlinked.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/PAdicSplitting/LocalGlobalCompatAtIwahoriFixedOfUnlinked.lean#L14). `ToTor` is in [InfLifts.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/PAdicSplitting/InfLifts.lean#L40), and `toTor` and `split_of_padic` in [PToTor.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/PAdicSplitting/PToTor.lean#L61).
