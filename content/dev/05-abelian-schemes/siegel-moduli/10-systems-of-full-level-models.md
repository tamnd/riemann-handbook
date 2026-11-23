---
title: Systems of full level models
decls:
  - GlobalTheory.SystemAmple.exists_system_ampFrames
  - GlobalTheory.T.exists_localModelSystem_ampleFrames_fullLevel
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Systems of full level models

[The theorem on local model systems](/entry/exists-local-systems-ample/) starts from a *system*: two models of full level for two different auxiliary primes, base models over each of them, and for every prime $p$ local models that are raised from base models. This section defines systems and proves that they exist when full level models exist. The construction collects the results of [the section on full level models](/entry/top-amp-exists/) and of [the section on base models](/entry/exists-base-model/), and it adds one more lemma, which raises a base model to a model of a local system. Two primes are needed because the auxiliary prime $n$ must be different from the residue characteristic $p$.

Fix a CM field $E$ with a host, a PEL datum $D$ and moduli spaces $X_l$ for all levels $l$, as in [the section on full level models](/entry/top-amp-exists/). For a prime $p$, a level $l$ good at $p$, a coefficient field $F$ of $l$ and a valuation ring $W \subseteq \mathbb{C}$ with $p$ in its maximal ideal, write $V_W = W \cap F$, as in [the section on local model systems](/entry/exists-local-systems-ample/). We use the rings $R_{S,A}$, the level compatibility of maps and the base models of [the previous section](/entry/exists-base-model/).

**Definition 5.10.1 (Prime to $p$ part of a level).** Let $l$ be a level with modulus $M$ and ideal $\mathfrak{M}$, and $p$ a prime. A level $l_0$ is the *prime to $p$ part* of $l$ if $A_0 = 1$, $M_0 = M / p^{v_p(M)}$ and $\mathfrak{M}_0 = \mathfrak{M} + M_0 \mathcal{O}_E$.

Lean: `GlobalTheory.Models.IsPrimeToPart`.

When $l$ is good at $p$, the prime to $p$ part exists and is unique, it divides $l$ (that is, $M_0 \mid M$, $\mathfrak{M} \subseteq \mathfrak{M}_0$ and $A_0 \mid A$), and $M_0$ is prime to $p$. This is a lemma of the chapter on levels, and we use it below.

**Definition 5.10.2 (Raised model).** Let $B$ be a base model at a level $l_0$, with projective model $C$ of $X_{l_0}$ over $R_{nM_0,1}$. Let $l$ be a level, $F$ a coefficient field of $l$, $\beta : O \to F$ a ring map and $Y$ a model of $X_l$ over $O$. Then $Y$ is *raised* from $B$ if there are a ring map $b : R_{nM_0,1} \to O$ that agrees with the inclusions into $F$, a map $r : X_{l,F} \to X_{l_0}$ and a map $\nu$ from the universal object of $X_l$, base changed to $F$, to that of $X_{l_0}$ over $r$, such that $(r, \nu)$ is compatible with the level and $Y$ is above $C$ over $(b, r, \nu)$.

Lean: `GlobalTheory.Models.Raises`.

So a raised model is finite over the base change of the base model, compatibly with $\eta$ and with the map of moduli spaces.

**Definition 5.10.3 (System).** A *system* for the moduli spaces $X_l$ consists of:

1. two auxiliary inert primes $n_0, n_1$ and integers $J_0, J_1 \ge 1$;
2. for $i = 0, 1$, a model $T_i$ of full level $n_i^{J_i}$ for $n_i$;
3. for $i = 0, 1$ and every level $l_0$ with $A_0 = 1$, a base model $B_i(l_0)$ of $T_i$ at $l_0$;
4. a choice $c(p) \in \{0, 1\}$ for each integer $p$, with $n_{c(p)} \ne p$;
5. for every prime $p$ and every valuation ring $W \subseteq \mathbb{C}$ with $p$ in its maximal ideal, a local system $Y^{p,W}$ at $(p, W)$;

such that for every $(p, W)$, every level $l$ good at $p$ and every coefficient field $F$ of $l$, the model $Y^{p,W}_{l,F}$ is raised from $B_{c(p)}(l_0)$, where $l_0$ is the prime to $p$ part of $l$.

Lean: `GlobalTheory.Models.System`.

**Theorem 5.10.4 (Systems with ample frames).** Assume the homomorphism extension theorem, the laws, the second laws, the third laws, and that full level models exist. Let $E$ be a CM field with a host, $D$ a PEL datum with $p_D + q_D \ge 1$ and $X_l$ moduli spaces for all levels, and assume the level compatibility for $D$. Then there is a system for the $X_l$ such that for $i = 0, 1$ there is $k_i$ with [ample frames](/entry/models-nonempty-z-on-of-components/) of level $(n_i^{k_i})^2$ for the semi-abelian scheme of $T_i$ and its line bundle.

Lean: `GlobalTheory.SystemAmple.exists_system_ampFrames` (also `GlobalTheory.T.exists_localModelSystem_ampleFrames_fullLevel`, a second name).

*Proof.* There are two different auxiliary inert primes $n_0 \ne n_1$: an auxiliary inert prime is an odd prime $n$ that is inert in $\mathbb{Q}(\sqrt{-d})$ and does not divide the [[discriminant|E0VZTNPJXA]] of $E$, and a lemma on primes gives such primes above every bound, since $d$ is a prime and $-d$ is a non-square modulo infinitely many primes. Take one prime $n_0$ and then a larger one $n_1$.

Since full level models exist, for $i = 0, 1$ there are $J_i \ge 1$, $k_i$ and a model $T_i$ of full level $n_i^{J_i}$ for $n_i$ with ample frames of level $(n_i^{k_i})^2$. For every level $l_0$ with $A_0 = 1$, [the theorem on base models](/entry/exists-base-model/) gives a base model $B_i(l_0)$ of $T_i$ at $l_0$, from the homomorphism extension theorem, the three sets of laws, the level compatibility and $J_i \ge 1$. We choose one for each $l_0$.

Put $c(p) = 0$ if $n_0 \ne p$ and $c(p) = 1$ if $n_0 = p$. In the second case $n_1 \ne n_0 = p$. So $n_{c(p)} \ne p$ in both cases.

Now fix a prime $p$, a valuation ring $W \subseteq \mathbb{C}$ with $p$ in its maximal ideal, a level $l$ good at $p$ and a coefficient field $F$ of $l$. Let $l_0$ be the prime to $p$ part of $l$. Then $l_0$ divides $l$ and $M_0$ is prime to $p$. Write $n = n_{c(p)}$. Since $n \ne p$ are primes, $n M_0$ is prime to $p$. A lemma on coefficient rings shows that $V_W$ is a [[Dedekind domain|7NPY2CN5KB]] of characteristic $0$ with fraction field $F$, and that every ring $R_{S, A}$ with $S$ prime to $p$ and $\zeta_A \in F$ maps into $V_W$ compatibly with the inclusions into $F$. This holds since $W \cap \mathbb{Q} = \mathbb{Z}_{(p)}$, in which $S$ is a unit. We apply it with $S = n M_0$ and $A = 1$, and get $b : R_{nM_0,1} \to V_W$.

A lemma on raised models, which uses the three sets of laws and the level compatibility, now gives a model $Y^{p,W}_{l,F}$ of $X_l$ over $V_W$ that is raised from $B_{c(p)}(l_0)$. Its inputs are $n > 0$, $l_0 \mid l$, the coefficient ring $V_W \to F$ and the map $b$. We choose one such model for each $(l, F)$; together they form the local system $Y^{p,W}$.

The primes $n_i$, the exponents $J_i$, the models $T_i$, the base models, the choice $c$ and the local systems form a system, and the ample frames of the $T_i$ come from the first step. $\square$

**Remark 5.10.5.** The models of a system depend on the choice of the base models, which uses choice. The theorem on local model systems does not need any compatibility between the base models $B_0(l_0)$ and $B_1(l_0)$ of the same level: for each $p$ it only uses the one with index $c(p)$.

**Remark 5.10.6 (Formalization).** The two primes come from the first part of `GlobalTheory.Models.exists_two_auxiliary_inert_odd_primes_coprime_level`; its second part, that an auxiliary prime is prime to every modulus, is discarded with `-` here and used inside the base models ([ExistsLocalModelSystemAmpleFramesFullLevel.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsLocalModelSystemAmpleFramesFullLevel.lean#L31)). The choice of $c(p)$ is `decide (n₀ = p)`. The prime to $p$ part comes from `GlobalTheory.Models.primeToPart_spec`, whose third part (monotonicity in the level) is discarded with `-` at line 51; the coefficient ring comes from `GlobalTheory.CoeffRings.coeff_isDedFrac`, with one part discarded at line 54; the raised models come from `GlobalTheory.LocalModelExists.exists_model_raises`. We followed the statements of these lemmas and did not open their proofs. The base models and local models are chosen with `Classical.choice` and `choose`. The second name is a wrapper proved by `first | exact @...` under `maxHeartbeats 1000000`.
