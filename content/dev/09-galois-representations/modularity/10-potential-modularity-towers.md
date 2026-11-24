---
title: Potential modularity towers and the seed in case III
decls:
  - UpperTheory.V.Th.eigenbasis_rank_four
  - UpperTheory.V.Th.local_zero_of_modular_p
  - UpperTheory.Gal.projectedFormsSystemPart.promodular_existence_of_local_zero
  - UpperTheory.Gal.projectedFormsSystemPart.pm_exists_of_unramified_adjoint_lifting
  - UpperTheory.V.HV.DescentVanishingReductions.pmEx_of_printsH
  - UpperTheory.V.Z.Win.Birth.fourth_initial_of_prints_h
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Potential modularity towers and the seed in case III

The symplectic image statement of [Theorem 8.7.5](/entry/sp4-in0-alt/) has five inputs. Two of them are proved in this section: the existence of potential modularity towers and the existence of seeds in case III. Both rest on Hida theory in rank four. The main step is an eigenbasis theorem: at a modular point of a Hida family, the Hecke ideal that cuts out the family contains every prime below the point. We keep the notation of the earlier sections: $l$ is an odd prime, $\iota \colon \overline{\mathbb{Q}}_l \to \mathbb{C}$ is an isomorphism, $\varepsilon$ is the cyclotomic character, and a tower $T$ comes with fields $F_T$, $L$ and a subgroup $G'$. As before, we state the predicates on towers and points in words and do not unfold them.

**Definition 8.10.1 (Hida setting).** A Hida setting over a CM field $L$ is an odd prime $l$, a complex conjugation $c$, the set of places of $L$ above $l$, a finite set of tame places, and an auxiliary place $v_0$. Fix a residual representation $r$ of rank $n$ over the residue field of a coefficient ring $\mathcal{O}$. The universal ordinary determinant ring of $r$ is a complete local $\mathcal{O}$-algebra $B$ with an algebra map from an Iwasawa algebra $\Lambda$ (a power series ring over $\mathcal{O}$). A point of $B$ is an $\mathcal{O}$-algebra map $x \colon B \to \overline{\mathbb{Q}}_l$, and it has a representation $\rho_x$ with determinant $x$.

**Definition 8.10.2 (Local zero).** Let $J$ be an ideal of $B$ and $x$ a point of $B$. The point $x$ is a local zero of $J$ if $J \subseteq \ker x$ and every prime ideal $\mathfrak{q} \subseteq \ker x$ of $B$ contains $J$.

So $x$ is a local zero of $J$ when $\operatorname{Spec} B/J$ contains every irreducible component of $\operatorname{Spec} B$ that passes through $x$.

We use one result of Hida theory as an input. In the earlier sections it is called the adjoint lifting theorem.

**Theorem 8.10.3 (Adjoint lifting).** Let $L$ be a CM field that does not contain a primitive $l$-th root of unity, fix a Hida setting over $L$, and let $2 \le n \le 4$. Let $x$ be a locally generic automorphic point of $B$ that is irreducible and has a flag at each place above $l$. Then the Bloch-Kato Selmer group of $\operatorname{ad} \rho_x$ is zero.

This statement is taken as given. The extended hypotheses supply it through [Theorem 8.16.4](/entry/core-alt-bis/), which a later section proves.

**Theorem 8.10.4 (Eigenbasis in rank four).** Fix a Hida setting over a CM field $L$ without a primitive $l$-th root of unity, with a large coefficient ring. Let $r$ have rank 4, and assume the adjoint lifting theorem. Let $J \subseteq B$ be an ideal with the Hida properties, and assume the conditions at $v_0$, on quadratic characters, and on the ratios of the residual characters. Let $x$ be a point of $B$ with $J \subseteq \ker x$. Suppose that $\rho_x$ is continuous, conjugate self-dual and automorphic, unramified at $v_0$, and irreducible on the kernel of the residual cyclotomic character. Suppose that its weights satisfy $m_j + 2 \le m_i$ for $i < j$, that it has a flag at each place above $l$, and that it meets the inertia condition. Then $x$ is a local zero of $J$.

Lean: `UpperTheory.V.Th.eigenbasis_rank_four`.

*Proof.* The Hida properties make $B$ finite and torsion free over $\Lambda$, and $\Lambda$ is a power series ring. Let $\mathfrak{q} \subseteq \ker x$ be a prime that does not contain $J$. Then there is a tangent vector $x'$ of $B$ at $x$ that is not a tangent vector of $B/J$. It gives a lift $\rho'$ of $\rho_x$ to the dual numbers, and so a cocycle $z$ of $\operatorname{ad} \rho_x$. The ordinary condition at the places above $l$ and the local conditions elsewhere show that $z$ is a Bloch-Kato class. The weight gaps and the freeness of the ratios of the characters make $x$ a locally generic point. So the adjoint lifting theorem applies: $z$ is a coboundary, $z(g) = \rho_x(g) X \rho_x(g)^{-1} - X$. Then $\rho'$ is conjugate to the constant lift, so $x'$ kills all traces. This contradicts the choice of $x'$. $\square$

**Theorem 8.10.5 (Local zero at a modular point).** Let $T$ be a tower with a Hecke ideal $J_0$, and let $\varphi$ be the map from the Hecke algebra of $T$ to $B$. Let $y$ be a seed point of $T$. Then $y$ is a local zero of $J = \varphi(J_0) B$.

Lean: `UpperTheory.V.Th.local_zero_of_modular_p`.

*Proof.* We check the hypotheses of the eigenbasis theorem at $y$. The weights of $\rho_y$ are those of the seed, and the seed condition $h_i = h_{i+1} + 2n$ with $n \ge 2$ gives $m_j + 2 \le m_i$. Irreducibility, continuity, the flag and the condition at $v_0$ come from the tower. Automorphy comes from the seed, through a twist by the character $\kappa$. The weights of $y$ show that $J \subseteq \ker y$. Then the eigenbasis theorem gives the result. $\square$

**Definition 8.10.6 (Potential modularity tower).** Let $D$ be raw data. A potential modularity tower for $D$ is a tower $T$ with a universal representation over a ring $B$ and an ideal $J$, with these properties. The ring $B/J$ is finite over $\mathcal{O}$. Every point of $B$ in characteristic $l$ is a local zero of $J$. The tower has a seed. Every point of $B/J$ over $\overline{\mathbb{Q}}_l$ satisfies the weak purity bound of the next section, and is automorphic. The statement "PM towers exist" says that each $D$ in case II or III has such a tower.

**Theorem 8.10.7 (Existence of potential modularity towers).** Assume the unramified inputs, and assume that every seed point of every tower is a local zero of its Hecke ideal. Then potential modularity towers exist.

Lean: `UpperTheory.Gal.projectedFormsSystemPart.promodular_existence_of_local_zero`.

*Proof.* Choose two links $K$ and $K'$ with the same character $\kappa$, at a prime $p$ that does not divide the level. Let $J_0$ and $J_0'$ be their Hecke ideals, and put $J = J_0 B + J_0' B$.

1. The ring $B/J$ is finite: a power of the maximal ideal lies in $J$, because each link is modular at $\varphi$.
2. A point in characteristic $l$ is a local zero of $J$: the hypothesis gives this for $J_0 B$ and $J_0' B$ at the seed points of the two links, and the deformation quotient is regular at the point.
3. The seeds of the two links give the seed of the tower.
4. Purity of the points of $B/J$ comes from the purity of the points of a link.
5. Automorphy comes from the two links. We glue the two automorphic representations at the place $v_0$, which is different for $K$ and $K'$, and descend.

$\square$

**Corollary 8.10.8 (Towers from adjoint lifting).** Assume the unramified inputs. Then potential modularity towers exist. Under the extended hypotheses, potential modularity towers exist.

Lean: `UpperTheory.Gal.projectedFormsSystemPart.pm_exists_of_unramified_adjoint_lifting` (also `UpperTheory.V.HV.DescentVanishingReductions.pmEx_of_printsH`, the form with the extended hypotheses).

*Proof.* By the theorem on local zeros, every seed point is a local zero. The existence theorem then gives the towers. Under the extended hypotheses, the rank $n$ package gives the unramified inputs and the adjoint lifting theorem. $\square$

**Theorem 8.10.9 (Seeds in case III).** Assume the extended hypotheses. Let $D$ be raw data in case III, $T_0$ a tower of $D$ of type four, and $k$ the residue field of an ambient coefficient datum. Then there are a prime $w$ that splits in $T_0$ and a residual representation $s$ over $k$ of the residual type of $T_0$ with the extra place $w$, with this property. For each larger tower $T \ge T_0$ in which $w$ dies, there is a representation $Q$ over a larger coefficient ring such that $Q$ is a seed pair, its reduction lies over $s$, and its entries at the roots $-w_{\beta}$ and $-w_{\theta}$ are not zero.

Lean: `UpperTheory.V.Z.Win.Birth.fourth_initial_of_prints_h`.

*Proof.* The seed is a tensor product. Let $K'$ be the imaginary quadratic field attached to the type four.

1. By the Eisenstein congruence of a later section, there are a prime $w$, a character $\theta$ with $\theta^l = 1$, a large weight $k$, and a modular 2-dimensional $\rho$ that is congruent to a sum of two characters. It has an integral model $\rho_1$.
2. An algebraic Hecke character $\kappa$ of $K'$ gives a 2-dimensional induced representation $\tau$.
3. Automorphy of tensor products: for a modular irreducible $\rho$ of this kind there is $j$ with $1 \le j \le 9$ such that $\rho \otimes \tau$ is automorphic over $K'$ for each $\tau$ built from $\kappa^j$. This follows from quadratic and solvable base change, automorphic induction, and the polarization of the tensor product.
4. The seed $Q$ is $\rho_1 \otimes \tau$, restricted to $G_F$. Its weights are the sums of the weights of $\rho_1$ and $\tau$. The large weight $k$ gives the gaps $2n$ with $n \ge 2$. The congruence of $\rho$ gives the residual type and the nonzero entries.

$\square$

**Remark 8.10.10 (Formalization).** The eigenbasis theorem and the existence theorem are in EigenbasisRankFour.lean and PmTwo.lean. The name `promodular_existence_of_local_zero` sits in the namespace `UpperTheory.Gal.projectedFormsSystemPart`, which says nothing about its content. The adjoint lifting theorem enters the eigenbasis theorem as a hypothesis `hAd`. The proof of the seed theorem in [BirthTop.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/BirthTop.lean#L82) is one call to `fourth_initial_of_rank_four_data` with fifteen inputs. The statement it proves is named `SeedIVAlt`, although it is the seed of case III. We have not unfolded the predicates `Four`, `Dies`, `OverT` and `InA`.
