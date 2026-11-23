---
id: strict-kill-main
title: An Euler system class kills the strict dual Selmer group
kind: theorem
decl: GlobalTheory.Ord2.StrictKill.main
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.StrictVanishingDualOfLiterature
covers: 302
status: drafted
drafted_by: writer@claude
---
This theorem shows that an Euler system class for a two-dimensional representation $W$ forces the strict Selmer group of the Tate dual $W^*$ to vanish. Under the name [`strict_vanishing_dual_of_literature`](/entry/strict-vanishing-dual-of-literature/) it is the first step of [`es_vanish`](/entry/es-vanish/). The proof pairs the two classes by a cup product and finds a nonzero number divisible by every power of $\ell$.

## Statement

Let $W \colon G_\mathbb{Q} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ satisfy $\mathrm{Nf}(e, S, A, W)$, as in [the unramified zeta theorem](/entry/zeta-ur/), and let $W^* = W \otimes \bar\chi\,(\det W)^{-1}$, with $\bar\chi$ the [[cyclotomic character|XSGB5K2KEG]]. Write $D_A$ for the [[decomposition group|7X92G8CQ33]] of the place $A$ above $\ell$, and $\omega(x, y) = x_1 y_2 - x_2 y_1$.

**Theorem.** Assume $\mathrm{LitCoh}$. If $\mathrm{ES}(W, A)$ holds, then every continuous cocycle $z$ of $W^*$ that is unramified at all primes $w \neq \ell$ and a coboundary on $D_A$ is a coboundary.

$\mathrm{ES}(W, A)$ gives an integral cocycle $y$ of $W$, unramified away from $\ell$, not ordinary at $A$, with tame derived classes at the primes $w \notin S'$ with $\ell^n \mid Nw - 1$ ([the zeta entry](/entry/zeta-ur/) states it).

## Proof

Suppose that $z$ is not a coboundary. Let $H = \ker\bar\chi \cap \ker\det W$ and $N = \ker\bar\chi \cap \ker W$.

1. **Integrality.** `galois_cocycle_integral_after_scaling` scales $y$ and $z$ by powers of $\ell$ to $y'$, $z'$ with values in one ring $\mathcal{O}$, with integral trivializations on inertia away from $\ell$ and, for $z'$, on $D_A$. `eulerSystemTameClass_scale_enlarge_coefficients` carries the tame classes to $y'$.
2. **Local triviality.** Let $\xi(s, t) = \omega(y'(s), W^*(s) z'(t))$, a 2-cocycle modulo $\ell^n$ with values in $\mathcal{O}(\bar\chi)$. At the place over $\ell$ it is a coboundary because $z'$ is trivial on $D_A$ (`cup_product_coboundary_mod`). At the other places of $S$ it is a coboundary because both classes are unramified (`cupProduct_unramifiedClasses_vanishes`).
3. **Gluing.** `local_cochains_glue_global` gives a cochain $u$ with $\xi \equiv du \pmod{\ell^n}$ on all of $G_\mathbb{Q}$.
4. **The height.** Let $\mathrm{ht}(\sigma) = \det(W(\sigma) - 1)\,u(\sigma) - \omega(\operatorname{adj}(W(\sigma) - 1)\,y'(\sigma), z'(\sigma))$. `cohomology_unramified_lift` uses the tame classes to show $\det(W(\sigma) - 1)\,\mathrm{ht}(\sigma) \equiv 0 \pmod{\ell^n}$ for $\sigma \in [H, H]$.
5. **Non-degeneracy.** $y'$ is not zero on $N$, or $y$ would be ordinary at $A$ (`greenbergOrdinary_of_vanishing_on_cycloKernel`). $z'$ is not zero on $N$, or $z$ would be a coboundary (`tateDual_cocycle_coboundary_of_vanish_on_fixing`). So `cocycle_pair_alternating_ne_on_cycloKernel` gives $g, h \in N$ with $\delta' = \omega(y'(h), z'(g)) - \omega(y'(g), z'(h)) \neq 0$. `exists_commutator_det_nonzero` gives $\varphi \in [H, H]$ with $\delta = \det(W(\varphi) - 1) \neq 0$.
6. **Conclusion.** `height_commutator_invariance` gives $\mathrm{ht}(\varphi[g, h]) - \mathrm{ht}(\varphi) \equiv \delta\delta' \pmod{\ell^n}$. Since $W(\varphi[g,h]) = W(\varphi)$, step 4 applies to both $\varphi$ and $\varphi[g,h]$. The ultrametric inequality gives $|\delta^2\delta'| \leq |\ell^n|$ for all $n \geq 1$, so $\delta^2\delta' = 0$, a contradiction.

The shape, a cup product of an Euler system class with a dual class and global reciprocity, is that of the Euler system method (K. Rubin, *Euler Systems*, Ann. of Math. Studies 147, 2000). We do not claim that this argument is in that book.

## In the Lean code

The theorem is at [line 162 of StrictVanishingDualOfLiterature.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/StrictVanishingDualOfLiterature.lean#L162). The cup product `cup` and the height `ht` are in [FinalTheorems.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/FinalTheorems.lean#L124). The lemmas above are `GlobalTheory.T.*`, each in a `…Statement.lean` file of the same folder; those of steps 2, 3 and 4 take $\mathrm{LitCoh}$. The file proves the small facts on $W^*$ itself: continuity (`cont_dual1`), integrality (`dual_representation_integral_entries`) and unramifiedness (`unr_dual1`). We have not unfolded the proofs of the lemmas in steps 2 to 5, nor the tame classes.
