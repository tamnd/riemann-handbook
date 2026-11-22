---
id: k4-top
title: Zeta classes of a newform glued into a norm-compatible cocycle system
kind: theorem
decl: UpperTheory.Kd.K4.top
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.NormProducts.AdmissibleWeightedDataMonoCoef
covers: 1491
status: drafted
drafted_by: writer@claude
---
This theorem makes, from a weighted sum of zeta systems of a newform, a norm-compatible family of cocycles $Y_r$ and one class $y$ with the local conditions of the unramified zeta argument. Under the name [`kato_eulerSystem_integrality`](/entry/kato-euler-system-integrality/) it is the hypothesis `h4` of [`kato_global_unit_law_of_smoothed_classes`](/entry/kato-global-unit-law-of-smoothed-classes/), on the way to [the unramified zeta theorem](/entry/zeta-ur/).

## Statement

Let $\ell$ be an odd prime, $\Omega$ an algebraic closure of $\mathbb{Q}$, $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, $e \geq 1$, $S$ a finite set of places and $A$ a valuation ring of $\Omega$. Let $W \colon G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ be a continuous [[Galois representation|JQEYEQJY2G]] with entries in the ring $\mathcal{O}$ of a coefficient datum, with the conditions `Nf`. Let $g$ be a newform of weight $2e+1$ with the conditions `SrcUr`. Let $X$ be a tower whose $j$-function is holomorphic on the set `Hs`. Let $N$ be prime to $\ell$, and let $c$, $d$, matrices $g_m(r_0) \in \Gamma_1(N)$, a function $\psi$ on $\mathbb{Z}/\ell$ and weights $c_w \colon \mathbb{Z}/N \to \overline{\mathbb{Q}}_\ell$, not all zero, satisfy `AdmWn`. Let $\rho$ be the twist of $W$ by a power of the cyclotomic character and by $\psi$ (the map `rhoK`), and $\kappa_r$ the inverse of the cyclotomic character mod $\ell^r$.

**Theorem.** There are integers $c_0, m$, a finite set of places $S'$, maps $Y_r \colon G_{\mathbb{Q}} \times (\mathbb{Z}/\ell^r)^\times \to \overline{\mathbb{Q}}_\ell^2$ and a map $y \colon G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^2$ such that:

1. $Y_r = \sum_x c_w(x)\, Y_{x,r}$, a sum of zeta systems for $X$ with exponent $c_0$ (`IsZWc`);
2. $Y_r(st, u) = Y_r(s, u) + \rho(s)\, Y_r(t, u\,\kappa_r(s))$;
3. $Y_r(s, u) = \sum_{u' \mapsto u} Y_{r+1}(s, u')$, the sum over the fibre of reduction mod $\ell^r$;
4. $Y_r$ is continuous in $s$, and for each $r, n$ there is a finite set $E_0 \subset \Omega$ with $|Y_r(ss', u)_1 - Y_r(s, u)_1| \leq |\ell^n|$ when $s'$ fixes $E_0$;
5. the values of $Y_r$ lie in $\mathcal{O}$;
6. $y(s) \equiv \sum_u \langle u \rangle^{-e} \chi_K(u)\, Y_r(s, u) \pmod{\ell^r}$ for each $r$, with $\langle u \rangle$ the least nonnegative lift of $u$ and $\chi_K$ the character `chiK` of $\psi$;
7. $\ell^m y$ satisfies `Sys` for $W$ and $S'$: it is an integral cocycle with the condition `Unr`, and it has tame classes (`Tame`) at the primes $w \notin S'$ with $\ell^n \mid Nw - 1$;
8. $\ell^m Y_r(\cdot)_1$ satisfies `IwSys2` for the character `nuD`, and $\ell^m Y$ and $\ell^m y$ satisfy `SpLink`.

The names point to the Euler system of K. Kato (Astérisque 295, 2004). We do not claim that this exact statement is in that paper.

## Proof

1. The lemma `g3` builds $Y$. For each $x$, the lemma `ml` gives a zeta system $Y_x$ with properties 2, 3, 5 and continuity, for each exponent $c_0 \geq c_1(x)$. Take $c_0 = \max_x c_1(x)$; `shCoc_wsum_props` shows that the weighted sum keeps the properties.
2. `GlobalTheory.K4.twist_clauses` writes $W = \theta\rho$ with $\theta$ a character, with integrality and congruence facts for the gluing step.
3. `kato_tame_relation_projected` gives an integer $k$, the set $S'$ and the tame relation at each prime $w \notin S'$, for $\ell^k Y$.
4. Replace $Y$ by $\ell^k Y$. The lemmas `shCoc_smul`, `push_smul`, `spec_smul` and `isZWc_raise` carry the properties over, with exponent $c_0 + k$.
5. `GlobalTheory.KZ.middle_glue2` takes all this and gives $m$, $y$ and a set of places, with properties 6, 7 and 8.
6. `exists_finset_unif` turns continuity in the Krull topology into the uniform clause 4.

The rest is bookkeeping.

## In the Lean code

The theorem is at [line 132 of AdmissibleWeightedDataMonoCoef.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/NormProducts/AdmissibleWeightedDataMonoCoef.lean#L132), and `g3` is at [line 15](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/NormProducts/AdmissibleWeightedDataMonoCoef.lean#L15).

Three things are odd. The hypothesis `SrcUr` on $g$ (line 133) is never used. The statement also asks for a second coefficient datum whose ring contains $\mathcal{O}$, but the proof takes the same datum (line 189), so that clause is trivial and we left it out above. And `AdmissibleNewformZetaData` takes an argument $x \in \mathbb{Z}/N$ that its body never uses ([AdmissibleNewformZetaData.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/AdmissibleNewformZetaData.lean#L15)), so `g3` gets the condition at every $x$ from the condition at one $x_0$ (line 28).
