---
title: The fibre criterion
decls:
  - UpperTheory.Et.E2.proper_base_change_closed_fibre
  - UpperTheory.Et.E2.proper_base_change_fibre
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The fibre criterion

Our proof of proper base change is an induction on towers of maps. Each step of a tower is a dominant map $c : Z \to S$ between AIC schemes, and we must move the closed fibre condition across $c$. This section proves the criterion that does this. If the closed fibre condition holds for $c$ after each base change to a strictly henselian point of $S$, then it holds for $Z \to \operatorname{Spec} A$ if and only if it holds for $S \to \operatorname{Spec} A$.

We keep the notation of the previous sections. In particular, for a local ring $A$ with residue field $\kappa$ and a map $p : X \to \operatorname{Spec} A$, $X_0$ is the closed fibre and $\mathrm{PB}_{q,i}(p)$ is the closed fibre condition.

### Two facts on AIC schemes

We use two facts on AIC schemes. Let $q$ be a unit on the schemes below.

1. *Degree zero.* Let $X$ be an AIC scheme and $f : Y \to X$ a map with $Y$ connected. Then $f^* : H^0(X, \mathbb{Z}/q(i)) \to H^0(Y, \mathbb{Z}/q(i))$ is bijective. Indeed $X$ contains the $q$-th roots of unity, so $\mathbb{Z}/q(i)$ is the constant sheaf $\mathbb{Z}/q$ on $X$ and on $Y$. By axiom A9, $H^0$ is the group of locally constant functions to $\mathbb{Z}/q$. Since $X$ is integral and $Y$ is connected, both groups are $\mathbb{Z}/q$, and $f^*$ is the identity of $\mathbb{Z}/q$.
2. *Acyclicity.* A qcqs AIC scheme $Z$ is acyclic: $H^n(Z, \mathbb{Z}/q(i)) = 0$ for $n > 0$. For a nonempty affine $Z$ the ring of $Z$ is an absolutely integrally closed domain, and axiom B5 applies. In general we use the induction principle of [the limit theorem](/entry/n17/) for qcqs schemes. Let $Z = U \cup V$ with $U$, $V$ quasi-compact open, and assume that $U$, $V$ and $U \cap V$ are acyclic. A nonempty open of an AIC scheme is an AIC scheme, and so it is connected. By fact 1, the map $H^0(U) \oplus H^0(V) \to H^0(U \cap V)$, $(a, b) \mapsto a - b$, is onto: it is $\mathbb{Z}/q \oplus \mathbb{Z}/q \to \mathbb{Z}/q$ when $U \cap V$ is nonempty, and its target is $0$ otherwise. The Mayer-Vietoris sequence then gives $H^n(Z) = 0$ for $n > 0$.

These two facts give a simple test for equivalences. By axiom A9, cohomology vanishes in negative degrees. So a map $f : E \to E'$ is an equivalence for $\mathbb{Z}/q(i)$ if $f^*$ is bijective on $H^0$ and both $E$ and $E'$ are acyclic. In particular, every qcqs map $c : Z \to S$ between qcqs AIC schemes is an equivalence, because an integral scheme is connected.

### The closed fibres

**Definition 3.5.1 (Strictly henselian point).** Let $S$ be a scheme. A *strictly henselian point* of $S$ is a map $t : \operatorname{Spec} B \to S$ where $B$ is a strictly henselian local ring. For a map $c : Z \to S$, the *base change* of $c$ to $t$ is the projection $c_t : Z \times_S \operatorname{Spec} B \to \operatorname{Spec} B$.

**Proposition 3.5.2 (Equivalence of closed fibres).** Assume the axioms A1 to A5, A7 to A10, B1 to B5 and E1. Let $A$ be a local ring with residue field $\kappa$, and let $q$ be a unit in $A$. Let $p : S \to \operatorname{Spec} A$ and $c : Z \to S$ be quasi-compact and quasi-separated, with $c$ dominant, and let $Z$ and $S$ be AIC schemes. Assume that $\mathrm{PB}_{q,i}(c_t)$ holds for every strictly henselian point $t : \operatorname{Spec} B \to S$ with $q$ a unit in $B$. Then the map of closed fibres $c_0 : Z_0 \to S_0$ is an equivalence for $\mathbb{Z}/q(i)$.

Lean: `UpperTheory.Et.E2.proper_base_change_closed_fibre`.

*Proof.* The map $c_0$ is the base change of $c$ along $S_0 \to S$, so it is quasi-compact and quasi-separated. The scheme $S_0$ is qcqs over $\operatorname{Spec} \kappa$, and $q$ is a unit on $S_0$.

Equivalences are Zariski local on the base. Precisely, we use the following fact, a consequence of the axioms. Let $f : Y \to X$ and $X \to T$ be qcqs maps, with $T$ qcqs and $q$ a unit on $T$. If for each point $s \in T$ the base change of $f$ to $\operatorname{Spec} \mathcal{O}_{T,s}$ is an equivalence, then $f$ is an equivalence. We apply it with $f = c_0$ and $X = T = S_0$.

So it is enough to show: for each $s \in S_0$, the base change of $c_0$ to $\operatorname{Spec} \mathcal{O}_{S_0, s}$ is an equivalence. This comes from the hypothesis on strictly henselian points, the two facts above and the axioms: we pass from the local ring $\mathcal{O}_{S_0, s}$ to its strict henselization, which is a cofiltered limit of étale neighbourhoods, and we use the hypothesis at the corresponding strictly henselian point of $S$. $\square$

**Theorem 3.5.3 (Fibre criterion).** Assume the axioms A1 to A5, A7 to A10, B1 to B5 and E1. Let $A$, $q$, $p : S \to \operatorname{Spec} A$ and $c : Z \to S$ be as in the proposition, with the same hypothesis on the strictly henselian points of $S$. Then
$$\mathrm{PB}_{q,i}(p \circ c) \iff \mathrm{PB}_{q,i}(p).$$

Lean: `UpperTheory.Et.E2.proper_base_change_fibre`.

*Proof.* Consider the commutative square of schemes
$$\begin{array}{ccc} Z_0 & \xrightarrow{j_Z} & Z \\ {\scriptstyle c_0} \downarrow & & \downarrow {\scriptstyle c} \\ S_0 & \xrightarrow{j_S} & S \end{array}$$
where $j_Z$ and $j_S$ are the inclusions of the closed fibres. It gives, in each degree $n$, the identity
$$j_Z^* \circ c^* = c_0^* \circ j_S^*$$
of maps $H^n(S, \mathbb{Z}/q(i)) \to H^n(Z_0, \mathbb{Z}/q(i))$.

The map $c^*$ is bijective by the test of the first part of this section: $Z$ and $S$ are AIC schemes, qcqs because $p$ and $p \circ c$ are qcqs, and $q$ is a unit on both. The map $c_0^*$ is bijective by [Proposition 3.5.2](/entry/proper-base-change-closed-fibre/).

Now $\mathrm{PB}_{q,i}(p \circ c)$ says that $j_Z^*$ is bijective, and $\mathrm{PB}_{q,i}(p)$ says that $j_S^*$ is bijective. If $j_Z^*$ is bijective, then $c_0^* \circ j_S^*$ is bijective, and since $c_0^*$ is bijective, so is $j_S^*$. If $j_S^*$ is bijective, then $j_Z^* \circ c^*$ is bijective, and since $c^*$ is bijective, so is $j_Z^*$. $\square$

**Remark 3.5.4.** The criterion does not ask $A$ to be strictly henselian. The strictly henselian rings enter only through the hypothesis on the points of $S$. In the next section the hypothesis comes from the case of curves over the projective line, which needs a strictly henselian base.

**Remark 3.5.5 (Formalization).** The two facts on AIC schemes are `UpperTheory.Et.E2.n45` and `UpperTheory.Et.E2.n49`. The Zariski local fact is `proper_base_change_zariski_local_to_global`, and the step at the local rings of $S_0$ is `closed_fibre_stalk_cohomology`. We checked these four results from their statements. The equivalence test and the two-out-of-three argument are in [FibClosed.lean](lean:Development/EtaleCohomology/EtaleSheaves/FibClosed.lean#L14).
