---
title: Moduli schemes at every level
decls:
  - GlobalTheory.ZM.moduli_of_deeper_level
  - GlobalTheory.T.nonempty_cmModuli_of_deeper_level
  - GlobalTheory.ZM.moduli_nonempty_all_levels
  - GlobalTheory.T.moduliScheme_nonempty_at_every_level
  - GlobalTheory.Moduli.moduli_scheme_exists
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Moduli schemes at every level

The earlier sections take the PEL moduli spaces $X_l$ as given, one for each level $l$. This section proves that they exist. That is the first part of condition N1 of [the section on local model systems](/entry/exists-local-systems-ample/). The proof has three moves. Moduli spaces exist at one special kind of level, with $M$ an odd prime $n$ and $A$ a power of $n$, by a construction from theta functions. They pass up from a level to every deeper level. And they pass down from a level to every level that divides it, as quotients by finite groups. The background is [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures).

Fix a CM field $E$ with a host and a PEL datum $D$. We use the levels, PEL objects and PEL moduli spaces of [the section on full level models](/entry/top-amp-exists/). Recall that a level $l$ *divides* a level $l_2$ if $M \mid M_2$, $\mathfrak{M}_2 \subseteq \mathfrak{M}$ and $A \mid A_2$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level.Dvd`.

The classical result is the following.

**Theorem 5.11.1 (Moduli of polarized abelian varieties with level structure).** Let $g \ge 1$, $d \ge 1$ and $N \ge 3$. The functor that sends a scheme $S$ over $\mathbb{Z}[1/dN]$ to the set of isomorphism classes of abelian schemes of relative dimension $g$ over $S$ with a polarization of degree $d^2$ and a level $N$ structure is represented by a quasi-projective scheme over $\mathbb{Z}[1/dN]$ (D. Mumford, J. Fogarty and F. Kirwan, *Geometric Invariant Theory*, Chapter 7).

The PEL moduli spaces of this chapter are defined differently. They live over the number field $K_A$; they represent the functor of PEL objects only on reduced schemes; and they carry the condition of infinitesimal rigidity in place of a full representability over all schemes. The results below prove their existence inside this chapter, without the classical theorem.

**Definition 5.11.2 (Quotient of a moduli space by a change of level).** Let $l \mid l_2$ be levels and $X_2$ a moduli space of level $l_2$. A *level quotient* of $X_2$ at level $l$ consists of:

1. a scheme $X$, quasi-projective over $K_A$ and smooth of relative dimension $\dim D$, with a PEL object of level $l$ over it;
2. a finite, [[étale|H84VHC8PX2]] and surjective map $\pi : X_2 \to X$ over an inclusion $K_A \subseteq K_{A_2}$ compatible with the inclusions into $\mathbb{C}$, with a map $m$ from the universal object of $X_2$ to the object of $X$ over $\pi$, which sends $\eta_2(a)^{M_2/M}$ to $\eta(a)$ and $\eta_{A_2}(a)^{A_2/A}$ to $\eta_A(a)$;
3. the fibre condition: if two geometric points $y, y'$ of $X_2$ lie over the same point of $\operatorname{Spec} K_{A_2}$, and the same object with the same level structure of level $l$ arises from both of them by lowering the level, then $\pi(y) = \pi(y')$.

Lean: `GlobalTheory.ZM.PEL.LevelQuot`, `GlobalTheory.ZM.PEL.Lowers`.

**Theorem 5.11.3 (Moduli at a lower level).** Assume the laws, the second laws and the theorem of the cube (for every polarized abelian scheme $A$ and every line bundle $M$ on $A$, the bundle $\Theta(M)$ on $A^3$ has a generating section). Let $l$ and $l_2$ be levels with $l \mid l_2$, and assume $p_D + q_D \ge 1$. If a moduli space of level $l_2$ exists, then a moduli space of level $l$ exists.

Lean: `GlobalTheory.ZM.moduli_of_deeper_level` (also `GlobalTheory.T.nonempty_cmModuli_of_deeper_level`, a second name).

*Proof.* Let $X_2$ be a moduli space of level $l_2$. A lemma on level quotients, which uses the laws, the second laws and the theorem of the cube, gives a level quotient $X$ of $X_2$ at level $l$. It is the quotient of $X_2$ by the finite group of level changes between $l$ and $l_2$, with the PEL object descended from the universal object of $X_2$. The scheme $X$ is quasi-projective over $K_A$, smooth of relative dimension $\dim D$, and carries an object of level $l$.

Two properties remain. First, $X$ represents PEL objects of level $l$ over reduced schemes: a lemma shows that every such object over a reduced scheme $S$ over $K_A$ is the pullback of the object of $X$ along exactly one map $S \to X$. The idea is that, étale locally on $S$, the level structure of level $l$ lifts to one of level $l_2$, which gives a map to $X_2$, and the fibre condition shows that the composite with $\pi$ does not depend on the lift. Second, $X$ is infinitesimally rigid at dual number points, by a second lemma; since $\pi$ is étale, rigidity passes from $X_2$ to $X$. So $X$ is a moduli space of level $l$. $\square$

**Theorem 5.11.4 (Moduli at every level).** Assume the laws, the second laws, the theorem of the cube and the uniformization theorem for complex abelian varieties. Then for every CM field $E$ with a host, every PEL datum $D$ with $p_D + q_D \ge 1$ and every level $l$, a moduli space of level $l$ exists.

Lean: `GlobalTheory.ZM.moduli_nonempty_all_levels` (also `GlobalTheory.T.moduliScheme_nonempty_at_every_level`, a second name).

*Proof.* Let $l$ be a level. A lemma on levels gives an odd prime $n$ such that for every $A_0 \ge 1$ there are levels $l_0$ and $l_2$ with $M_0 = n$, $A$-part $A_0$, $l_0 \mid l_2$ and $l \mid l_2$. So $l_2$ is a common deeper level of $l$ and of a level with modulus $n$.

A lemma on full level moduli, which uses the laws, the second laws, the theorem of the cube and the uniformization theorem, gives $j$ such that a moduli space exists at every level with $M = n$ and $A = (n^j)^2$. This is where the moduli spaces are built, from theta functions of level $(n^j)^2$; the uniformization theorem enters only here.

Take $A_0 = (n^j)^2$ and the levels $l_0$ and $l_2$ from the first step. A moduli space exists at level $l_0$. A lemma on deeper levels, which uses the laws and the second laws, gives a moduli space at level $l_2$, since $l_0 \mid l_2$. Now the previous theorem gives a moduli space at level $l$, since $l \mid l_2$. $\square$

**Corollary 5.11.5 (Existence of the moduli schemes).** For every CM field $E$ with a host, every PEL datum $D$ with $p_D + q_D \ge 1$ and every level $l$, a moduli space of level $l$ exists.

Lean: `GlobalTheory.Moduli.moduli_scheme_exists`.

*Proof.* This is the previous theorem applied to the laws and the second laws, which are the first two of the six laws of abelian schemes, to the theorem of the cube for polarized abelian schemes and to the uniformization theorem for complex abelian varieties, which are proved elsewhere in the proof. For the background see [the theorem of the cube](/learn/abelian-varieties/#the-theorem-of-the-cube) and [the complex uniformization](/learn/abelian-varieties/#the-complex-uniformization). $\square$

**Remark 5.11.6.** The detour through the level $l_2$ is needed because the theta construction gives moduli spaces only at levels with $M = n$ prime and $A$ a square of a power of $n$. A general level $l$ has a modulus $M$ with several prime factors, and the common deeper level $l_2$ has modulus divisible by $nM$. So the order of the three moves matters: first up from $l_0$ to $l_2$, then down from $l_2$ to $l$.

**Remark 5.11.7 (Formalization).** The first part of condition N1 is the proposition `N1ab` in [HeckeKer.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/HeckeKer.lean#L10); it asks only for `Nonempty (Moduli D l)`, so the theorems give existence, not a chosen moduli space. The theorem of the cube is the hypothesis `∀ S P M, M.IsLB → ∃ t : LB.Gen (Theta P.A M), t.IsGen`, and the uniformization theorem is `ThetaUnifAV`. In the theorem on lower levels, the theorem of the cube is used only by `T.nonempty_levelQuot_of_level_dvd`; the two properties come from `T.levelQuotient_represents_reduced` and `T.levelQuotient_unramified_dualNumberPoints`. In the theorem on every level, the uniformization theorem is used only by `T.exists_moduli_prime_power_fullLevel`; the other lemmas are `T.exists_level_with_odd_prime_first_number` and `T.nonempty_moduli_of_level_dvd`. We followed their statements and did not open their proofs, so the sketches of the construction in the two proofs above are a reading of these statements. The corollary takes the laws from `T.all_six_abelian_scheme_laws_hold`. The second names are wrappers proved by `first | exact @...` under `maxHeartbeats 1000000`.
