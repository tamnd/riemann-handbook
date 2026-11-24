---
title: Height bounds for points of good towers
decls:
  - GlobalTheory.T.good_tower_I5
  - GlobalTheory.CompanionTheory.Ar.Top.i5_and_i6_of_isGlobal_of_goodOrigin
  - RootFieldNumerics.global_model_tower_fifth_condition
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Height bounds for points of good towers

The successive minima inequalities turn bounds for the heights of points into bounds for top intersection numbers. The chain of [tower estimates](/entry/chain-tower/) needs two such bounds for the twisted root lines: a lower bound $-C \log(B/s)$ for the height of every point (I5), and an upper bound $C \log B$ on a Zariski dense set of points (I6). This section proves both for good towers over global integral models. The proof reduces them to a local condition at each prime of $S_B$, the sandwich of the Hodge component, which follows from the Fargues comparison for Hodge-Tate lattices. The result is used in [the volume theorem](/entry/volume-theorem-x-of-inputs/).

We use the setting of [the chapter on good towers](/entry/good-tower-volume-of-reduced/). Let $E$ be a CM field with host $H$, and let $\Psi$ be the set of CM types of $H$. Let $D$ be a hermitian datum of signature $(p, q)$, let $X_o$ be a family of moduli spaces for $D$ indexed by the levels of $H$, let $l$ be a level with coefficient field $c$, and let $Y$ be an integral model of $X_o(l)$. The model $Y$ is global if it carries, at every prime $p$ and every valuation ring of $\mathbb{C}$ above $p$, a local system with split fibres and the further conditions of [the chapter on good towers](/entry/good-tower-volume-of-reduced/), if the level is good at every prime, and if $Y$ descends; we use these conditions only through the results we cite. A good origin of a root tower $T$ of type $(\Psi, p+q)$ over $Y$ is the datum built in [the existence theorem for good root towers](/entry/exists-good-root-tower/): for each level $B$ a finite set of primes $S_B$, for each component $c$ a Hodge component of $Y$ over $S_B$ whose coordinates are those of $M_{B, c}$, a flag datum and root line data, and a reference root model independent of $B$. The extra conditions are those of that theorem.

Let us recall what the two bounds say. Fix $c_0 > 0$. For a rational weight $\lambda$ with $\|\lambda\|_\infty \le 1$, compact gaps at least $c_0$ and $j$-gaps at least $\theta$, and for $s = \theta^2$, the twisted line $L_{\lambda_s, s}$ on $M_{B,c}$ is a combination of the root lines and the ample line $A$. Since the root lines are graded pieces of the Hodge flag, its height at a point $W$ is a combination of heights of graded pieces of the Lie bundle at the corresponding point of $Y$. I5 bounds these heights from below for every point, and I6 bounds them from above on a Zariski dense set.

The local input is the sandwich. Let $\ell \in S_B$ and let $\mathfrak{M}$ be a Hodge component over $S_B$. A sandwich of $\mathfrak{M}$ at $\ell$ with constant $\kappa$ compares, up to the factor $\kappa$, the Lie lattice at $\ell$ with the lattice of the flag basis of $\mathfrak{M}$, as in the flag sandwich of the chapter on good towers. The Hodge component is Hodge-Tate free at $\ell$ if the module of invariant differentials at $\ell$ is a vector bundle of the full rank on the fibre at $\ell$, and each of its images under the dual restrictions to the labels is a vector bundle of the rank of the label. The Fargues comparison, applied to these bundles, gives a sandwich with a constant $\kappa \in \mathbb{C}_\ell$.

We take three of the top level inputs as given:

1. the resolution statement for residue fields;
2. the Fargues comparison for Hodge-Tate lattices, which rests on the integral Hodge-Tate theory of $p$-divisible groups of Fargues (see the notes at the end of the chapter);
3. the GAGA input for flat sections.

The first and the third give the flat line generator input: every flat hermitian line on the analytic space of a component has a generator, which is flat. We also use that a good origin gives split components for $Y$, and that each Hodge component of a good origin at $(B, c)$ is Hodge-Tate free at every prime of $S_B$.

**Theorem 9.6.1 (I5 and I6 for good towers).** Assume the top level inputs. Let $E$ be a CM field, abelian over $\mathbb{Q}$, with host $H$, let $D$ have signature $(p, q)$, and let $Y$ be an integral model of $X_o(l)$. Let $T$ be a root tower of type $(\Psi, p + q)$ with a good origin over $Y$, and let $\mathrm{II}$ be an intersection system. Assume that $Y$ is global, that the origin satisfies the extra conditions, that $\mathrm{II}$ is full and that $p, q \ge 1$. Then $T$ satisfies I5 and I6.

Lean: `RootFieldNumerics.global_model_tower_fifth_condition` (also `GlobalTheory.CompanionTheory.Ar.Top.i5_and_i6_of_isGlobal_of_goodOrigin` and `GlobalTheory.T.good_tower_I5`, second names)

*Proof.* We apply the [theorem on good towers from sandwiches](/entry/tower-good-of-sandwich-split/). Its hypotheses are the top level inputs, the flat line generator input, split components of $Y$, a good origin, an intersection system, and a sandwich at each prime of $S_B$ for every level and component.

The top level inputs are given. The flat line generator input follows from the resolution statement and the GAGA input. The good origin gives the split components of $Y$ from its tower origin. A full intersection system is in particular an intersection system.

Fix a level $B$, a component $a$ and a prime $\ell \in S_B$. The primes of $S_B$ are prime numbers, so $\ell$ is prime. The good origin says that the Hodge component $\mathfrak{M}$ at $(B, a)$ is Hodge-Tate free at $\ell$. Since $p \ge 1$, we have $p + q > 0$. The Fargues comparison then gives $\kappa \in \mathbb{C}_\ell$ such that $\mathfrak{M}$ has a sandwich at $\ell$ with constant $\kappa$.

So all hypotheses hold, and $T$ satisfies I5 and I6. $\square$

In the theorem on good towers from sandwiches, the sandwiches make the reference root models of the origin close to $T$, and the closeness gives I6 directly. For I5 the reference models need an ample line, flat units and the fibre input; the fibre input is the statement that every point of a root model lifts to an orthogonal flag pair of the Lie bundle over the ring of integers of a finite extension, and it gives the lower bound for heights of points.

**Remark 9.6.2 (Formalization).** Three hypotheses are not used: that $Y$ is global, the extra conditions of the origin, and $q \ge 1$. Of the fullness of $\mathrm{II}$ only the first part, that it is an intersection system, is used, and $p \ge 1$ is used only for $p + q > 0$. The hypothesis that $E$ is abelian over $\mathbb{Q}$ is not needed by the results the proof calls. The three inputs are taken from the top level inputs by position, as the fifth, seventh and eighth parts ([GlobalModelTowerFifthCondition.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/GlobalModelTowerFifthCondition.lean#L24)). The name speaks of a fifth condition, but the conclusion is the pair I5 and I6. The two other names are relays with the same statement. We have not unfolded the definition of a sandwich, the conditions of a global model or the proof of the Fargues step; the description of the sandwich is our reading.
