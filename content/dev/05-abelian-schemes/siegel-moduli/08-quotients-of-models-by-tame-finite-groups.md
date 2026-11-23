---
title: Quotients of models by tame finite groups
decls:
  - GlobalTheory.Models.exists_quotient_model
  - GlobalTheory.T.exists_quotient_model_by_tame_finite_group
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Quotients of models by tame finite groups

The models of full level of [the section on full level models](/entry/top-amp-exists/) have a deep level $A = n^J$. The local model systems of [the previous section](/entry/exists-local-systems-ample/) need models of the moduli spaces $X_{l_0}$ with $A = 1$. The moduli space of level $l_0$ is the quotient of the moduli space of a deeper level by a finite group. This section proves that a projective model of the deeper level, with an action of that group, descends to a projective model of the quotient, provided that the action is *tame*: every stabilizer has order prime to the residue characteristic, and acts trivially on the fibre of the semi-abelian scheme at its fixed point. The background is [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures) and [semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction).

Fix a CM field $E$ with a host. All semi-abelian schemes carry an $\mathcal{O}_E$-action and a line bundle $L$, as in [the section on the tangent space](/entry/finrank-derivation-le/).

**Definition 5.8.1 (Coefficient ring).** A ring map $\beta : O \to F$ to a field is a *coefficient ring* if $O$ is a [[Dedekind domain|7NPY2CN5KB]] of characteristic $0$ and $\beta$ makes $F$ the fraction field of $O$.

Lean: `GlobalTheory.Models.IsDedFrac`.

**Definition 5.8.2 (Projective model of a family).** Let $U$ be a scheme over a field $F$ through $c : U \to \operatorname{Spec} F$, let $t_0$ be a semi-abelian scheme with $\mathcal{O}_E$-action over $U$, and let $\beta : O \to F$ be a ring map. A *projective model* $C$ of $(U, t_0)$ over $O$ consists of:

1. a normal scheme $X$ with a map $s : X \to \operatorname{Spec} O$ that is projective and [[Flat|5M6KS8F47R]];
2. an [[open immersion|GFC5YKSN5H]] $j_F : U \to X \times_O F$ over $F$ with dense image; we write $j : U \to X$ for its composite with the projection;
3. a semi-abelian scheme $t$ with $\mathcal{O}_E$-action over $X$ and a map $m : t_0 \to t$ over $j$;

such that the abelian locus of $t$, pulled back to the generic fibre $X \times_O F$, is exactly the image of $j_F$.

Lean: `GlobalTheory.Models.Cpt`, `GlobalTheory.Models.Cpt.j`.

A model of a moduli space in the sense of [the previous section](/entry/exists-local-systems-ample/) is a projective model of $(X_{l,F}, G^{\mathrm{univ}})$. The last condition says that $j$ sees exactly the part of the generic fibre where $G$ is an abelian scheme. So the boundary $X_F \setminus j(U)$ is the place where $G$ degenerates, as for a toroidal compactification.

**Definition 5.8.3 (A model above another).** Let $C'$ be a projective model of $(U', t_0')$ over $O'$ and $C$ one of $(U, t_0)$ over $O$. Let $b : O \to O'$ be a ring map, $r : U' \to U$ a map and $\nu : t_0' \to t_0$ a map over $r$. Then $C'$ is *above* $C$ over $(b, r, \nu)$ if there are a map $\pi : X' \to X$ over $\operatorname{Spec} b$ such that the induced map $X' \to X \times_O O'$ is finite, and a map $\mu : t' \to t$ over $\pi$, with $\pi \circ j' = j \circ r$ and $\mu \circ m' = m \circ \nu$.

Lean: `GlobalTheory.Models.Cpt.Above`.

A model $C$ has *good* semi-abelian scheme if $t$ is [good](/entry/models-nonempty-z-on-of-components/): its abelian locus is open with $G$ proper over it, its fibres split after a finite separable extension of the residue field, and locally there are sections of $L$ that do not vanish together on any fibre.

**Definition 5.8.4 (Invertible pushforward).** Let $G \to X$ be a semi-abelian scheme with line bundle $L$. The pushforward of $L$ is *invertible* if every point of $X$ has an open neighbourhood $V$ with sections $\theta$ of $L$ over $G_V$, which do not vanish together at any point of any fibre over $V$, such that for every open $W \subseteq V$ each section of $L$ over $G_W$ is $a \theta$ for exactly one function $a \in \mathcal{O}(W)$.

Lean: `PushInvertible`.

This says that $\pi_* L$ is a line bundle on $X$, generated near each point by one section $\theta$. For a principal polarization of an abelian scheme this is the usual statement $h^0(L_x) = 1$ on every fibre.

**Theorem 5.8.5 (Quotient of a model by a tame finite group).** Let $U$ and $U'$ be schemes over fields $F$ and $F'$, through $c$ and $c'$, with semi-abelian schemes $t_0$ over $U$ and $t_0'$ over $U'$. Let $\beta : O \to F$ and $\beta' : O' \to F'$ be coefficient rings. Let $\Gamma$ be a finite group and $C$ a projective model of $(U, t_0)$ over $O$. Let $b : O' \to O$ and $k : F' \to F$ be ring maps with $\beta \circ b = k \circ \beta'$ and $\operatorname{Spec} b$ finite. Let $r : U \to U'$ be a map with $c' \circ r = \operatorname{Spec}(k) \circ c$ and $\nu : t_0 \to t_0'$ a map over $r$. Let $\rho_0 : \Gamma \to \operatorname{Aut}(U)$, $\tau_0 : \Gamma \to \operatorname{Aut}(G_0)$, $\rho : \Gamma \to \operatorname{Aut}(X)$ and $\tau : \Gamma \to \operatorname{Aut}(G)$ be homomorphisms, and for each $g \in \Gamma$ let $\mu_g$ be a map of semi-abelian schemes $t \to t$ over $\rho(g)$. Assume:

1. $U'$ is the quotient $U / \Gamma$ through $r$: the map $r$ is affine, $r \circ \rho_0(g) = r$ for all $g$, and for every open $V \subseteq U'$ the map $\mathcal{O}(V) \to \mathcal{O}(r^{-1} V)$ is injective, with image the functions fixed by every $\rho_0(g)$;
2. $G_0$ is [[proper|9537RKBZPP]] over $U$;
3. for every $g$, the map underlying $\mu_g$ is $\tau(g)$, $\rho(g) \circ j = j \circ \rho_0(g)$, $\tau(g) \circ m = m \circ \tau_0(g)$ and $\nu \circ \tau_0(g) = \nu$;
4. $G$ is quasi-projective over $O$;
5. for every algebraically closed field $K$ and every point $x \in X(K)$, the order of the stabilizer $\{g : \rho(g) \circ x = x\}$ is nonzero in $K$;
6. for such $x$ and every $g$ that fixes $x$, the map $\tau(g)$ is the identity on the fibre $G_x$;
7. $t$ is good and the pushforward of $L$ is invertible.

Then there is a projective model $C'$ of $(U', t_0')$ over $O'$ whose semi-abelian scheme is good, such that $C$ is above $C'$ over $(b, r, \nu)$.

Lean: `GlobalTheory.Models.exists_quotient_model` (also `GlobalTheory.T.exists_quotient_model_by_tame_finite_group`, a second name).

*Proof.* We build the quotient scheme, then the semi-abelian scheme on it, then the map from $t_0'$, and last we check the abelian locus.

First, the quotient. Since $X$ is projective over $O$, every orbit of $\Gamma$ lies in an affine open set, and the quotient $X' = X / \Gamma$ exists with a finite map $\pi : X \to X'$ (A. Grothendieck, SGA 1, Exposé V, §1). The ring $O'$ maps to the invariants through $b$, since $\Gamma$ acts over $O$ and $\operatorname{Spec} b$ is finite. Then $X'$ is normal (invariants of a normal domain are normal), projective and flat over $O'$. The relation $\rho(g) \circ j = j \circ \rho_0(g)$ makes $j$ pass to the quotients: by hypothesis 1, $U' = U / \Gamma$, and we get a dense open immersion $j'_{F'} : U' \to X' \times_{O'} F'$ with $\pi \circ j = j' \circ r$.

Second, the semi-abelian scheme. The group $\Gamma$ acts on $G$ over its action on $X$, through $\tau$. Hypotheses 5 and 6 say that this action is tame and that each stabilizer acts trivially on the fibre at its fixed point. Under these conditions $G / \Gamma$ is a semi-abelian scheme $t_1$ over $X'$ with $G \cong \pi^* G_1$, and $L$ descends with its cubical structure. Goodness descends: the abelian locus is the image of the abelian locus of $G$, the split fibres come from those of $G$ because $\pi$ is finite, and the sections $\theta$ of the invertible pushforward, averaged over the stabilizers, give local sections of the descended bundle that do not vanish together on fibres. This uses hypothesis 7 and the quasi-projectivity of $G$ in hypothesis 4.

Third, the map from $t_0'$. Compose $m$ with $G \to G_1$. By hypothesis 3, the result is invariant under $\tau_0$, and $\nu$ is invariant too. Since $G_0$ is proper over $U$ and $U \to U'$ is the quotient, the map descends along $\nu$ to a map $m' : t_0' \to t_1$ over $j'$.

Last, the abelian locus. Since $\pi$ is integral and surjective, and $G \cong \pi^* G_1$, a point $x \in X$ lies in the abelian locus of $G$ if and only if $\pi(x)$ lies in that of $G_1$. Let $w$ be a point of the generic fibre of $X'$ in the abelian locus. Choose $x$ over it. Because $O' \to O$ is finite and injective, $x$ lies over the generic point of $\operatorname{Spec} O$, so $x$ is in the generic fibre of $X$ and in the abelian locus of $G$. By the last condition on $C$, the point $x$ is in the image of $j_F$, so $w$ is in the image of $j'_{F'}$. The converse holds because $r$ is surjective. So $C' = (X', j', t_1, m')$ is a projective model with good semi-abelian scheme, and $(\pi, \mu)$ shows that $C$ is above $C'$. $\square$

**Remark 5.8.6.** The tameness conditions 5 and 6 cannot be left out. If a stabilizer has order divisible by the residue characteristic $p$, the quotient of a smooth group scheme by it need not be smooth. If a stabilizer acts on a fibre of $G$ by a nontrivial automorphism, the quotient of $G$ is not a group scheme over $X'$ with that fibre. In the application, $\Gamma$ is a group of level changes of $n$-power order, and $n$ is a unit on the base.

**Remark 5.8.7 (Formalization).** The coefficient rings are `IsDedFrac`, which asks for a Dedekind domain of characteristic zero and `IsFractionRing` through `β.toAlgebra`. The proof uses `GlobalTheory.exists_quotient_model_scheme` for the quotient scheme, `GlobalTheory.T.exists_semiAbelian_descent_tame_quotient` for the semi-abelian scheme and its goodness, `GlobalTheory.T.exists_cmTripleMap_descend_groupQuotient` for the map $m'$ and `GlobalTheory.quotient_isIntegral_surjective_orbits` for the surjectivity of $\pi$ and $r$ ([ExistsQuotientModelByTameFiniteGroup.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsQuotientModelByTameFiniteGroup.lean#L102)). We did not open the proofs of these three descent lemmas; the first two steps of the proof above describe what their statements give. The second name is a wrapper proved by `first | exact @...` under `maxHeartbeats 1000000`.
