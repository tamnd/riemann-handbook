---
title: Quotients of absolutely integrally closed domains
decls:
  - UpperTheory.Et.E2.n78
  - UpperTheory.Et.E2.n82
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Quotients of absolutely integrally closed domains

The next five sections prove the proper base change theorem. The proof reduces the theorem to schemes whose rings of sections are absolutely integrally closed. Axiom B5 says that an absolutely integrally closed domain is acyclic. In this section we extend this to every quotient $B/I$ of such a domain. The closed fibres that occur later are of this form, so this is the main input for the cohomology of fibres.

We fix the setting of the proper base change proof. Let $q \geq 1$ and $i \in \mathbb{Z}$. All rings and schemes are small for a fixed universe, and we use the model and the axioms of the first section.

**Definition 3.2.1 (The closed fibre condition).** Let $A$ be a local ring with residue field $\kappa$, and let $p : X \to \operatorname{Spec} A$ be a map of schemes. Let $X_0 = X \times_{\operatorname{Spec} A} \operatorname{Spec} \kappa$ be the closed fibre and $j : X_0 \to X$ the first projection. We say that $p$ satisfies the *closed fibre condition* for $(q, i)$ if $j$ is an equivalence for $\mathbb{Z}/q(i)$, that is, if
$$j^* : H^n(X, \mathbb{Z}/q(i)) \to H^n(X_0, \mathbb{Z}/q(i))$$
is bijective for every $n$. We write $\mathrm{PB}_{q,i}(p)$.

**Definition 3.2.2 (AIC scheme).** A scheme $Z$ is an *AIC scheme* if $Z$ is integral and the ring $\Gamma(U, \mathcal{O}_Z)$ is absolutely integrally closed for every nonempty affine open $U \subseteq Z$.

For example, $\operatorname{Spec} B$ is an AIC scheme for each absolutely integrally closed domain $B$, because a localization $B_f$ with $f \neq 0$ is again an absolutely integrally closed domain.

**Theorem 3.2.3 (Quotients are acyclic).** Let $B$ be an absolutely integrally closed domain, let $q$ be a unit in $B$, and let $I \subseteq B$ be an ideal. Assume the axioms A1 to A5, A7 to A10, B1 to B5 and E1. Then $\mathrm{sp}(B/I)$ is acyclic for $q$: for all $n > 0$ and all $i$,
$$H^n(\mathrm{sp}(B/I), \mathbb{Z}/q(i)) = 0.$$

Lean: `UpperTheory.Et.E2.n78`.

The proof needs a henselian ring with the same quotient as $B$. Recall that a pair $(C, K)$ of a ring and an ideal is *henselian* if $K$ is in the Jacobson radical of $C$ and each monic polynomial over $C$ whose reduction mod $K$ has a simple root has a root in $C$ that lifts it ([Hensel's lemma](/learn/algebra/#rings-ideals-and-modules), [[Hensel's lemma|010QVB71T2]]).

**Lemma 3.2.4 (A henselian model of the quotient).** Let $B$, $q$ and $I$ be as in the theorem. There is a filtered diagram of rings $(D_j)_{j \in J}$ with colimit $C$, and an ideal $K \subseteq C$, with these properties.

1. Each $D_j$ is isomorphic to a finite product $\prod_k R_k$ of absolutely integrally closed domains $R_k$ in which $q$ is a unit.
2. $q$ is a unit in $C$, and the pair $(C, K)$ is henselian.
3. There is a ring isomorphism $B/I \cong C/K$.

Lean: `UpperTheory.Et.E2.n82`.

*Proof.* We build the diagram from the idempotents of $B/I$. A *partition* of a ring $A$ is a finite set $P$ of nonzero idempotents of $A$ that are pairwise orthogonal and have sum $1$. A partition $Q$ *refines* $P$ if each $e' \in Q$ satisfies $e' e = e'$ for some $e \in P$. Two partitions $P$ and $Q$ have the common refinement formed by the nonzero products $e e'$, so the partitions of $B/I$ form a filtered category $J$. For an idempotent $e$ of $B/I$ let
$$S_e = \{ s \in B : \bar{s} t e = e \text{ for some } t \in B/I \},$$
the elements of $B$ whose image is a unit on the piece $e$. It is a multiplicative set, and $0 \notin S_e$ because $e \neq 0$. For a partition $P$ put
$$D_P = \prod_{e \in P} B[S_e^{-1}],$$
with the diagonal map $\beta_P : B \to D_P$. If $Q$ refines $P$ and $e' e = e'$, then $S_e \subseteq S_{e'}$, and the maps $B[S_e^{-1}] \to B[S_{e'}^{-1}]$ give a map $D_P \to D_Q$. This is the diagram.

*Property 1.* Each $B[S_e^{-1}]$ is a localization of the domain $B$ at a set that does not contain $0$. So it is a domain, and it is absolutely integrally closed: a monic polynomial over $B[S_e^{-1}]$ becomes monic over $B$ after we scale the variable by a common denominator, and a root in $B$ gives a root in $B[S_e^{-1}]$. The element $q$ stays a unit.

*Three properties of each stage.* First, $B/I \to D_P / I D_P$ is bijective. Indeed $D_P/ID_P = \prod_{e \in P} (B/I)[\bar{S}_e^{-1}]$. A lift of $e$ lies in $S_e$, so $e$ becomes a unit in the factor at $e$, and then $e(1 - e) = 0$ gives $1 = e$ there. Each element of $\bar{S}_e$ is already a unit in $(B/I)e$. So the factor at $e$ is $(B/I)e$, and $B/I = \prod_{e \in P} (B/I) e$. Second, for $x \in I D_P$ the element $1 + x$ is a unit in $D_P$: in the factor at $e$ we have $x = a/s$ with $a \in I$ and $s \in S_e$, and $1 + x = (s + a)/s$ with $s + a \in S_e$ because $s + a \equiv s \bmod I$. Third, let $f \in D_P[x]$ be monic and $a_0 \in D_P$ with $f(a_0) \in I D_P$ and $f'(a_0)$ a unit mod $I D_P$. We work in one factor $R = B[S_e^{-1}]$. Since $R$ is an absolutely integrally closed domain, $f = \prod_{l=1}^{m} (x - r_l)$ with $r_l \in R$. Put $y_l = a_0 - r_l$. Then modulo $I$ we have $\prod_l y_l = f(a_0) = 0$ and $\sum_l \prod_{m' \neq l} y_{m'} = f'(a_0)$, a unit. Let $u$ be this unit and put $\varepsilon_l = u^{-1} \prod_{m' \neq l} y_{m'}$ in $(B/I)e$. Then $\sum_l \varepsilon_l = e$, and $\varepsilon_l y_l = 0$ and $\varepsilon_l \varepsilon_k = 0$ for $l \neq k$, since each of these products contains $\prod_l y_l$. So $\varepsilon_l = \varepsilon_l \sum_k \varepsilon_k = \varepsilon_l^2$, and the $\varepsilon_l$ are orthogonal idempotents. We refine $P$ by the nonzero $\varepsilon_l$, and on the piece $\varepsilon_l$ we take the root $a = r_l$. Then $a - a_0 = -y_l$ lies in $I$ on that piece. So $f$ has a root $a$ in a later stage $D_Q$ with $a - a_0 \in I D_Q$.

*The colimit.* Let $C = \varinjlim_P D_P$ and let $K = I C$. Every element and every polynomial over $C$ comes from some $D_P$, so the second and third properties pass to $(C, K)$: $K$ lies in the Jacobson radical of $C$, and simple roots mod $K$ of monic polynomials lift. So $(C, K)$ is henselian. The maps $B/I \to D_P/ID_P$ are all bijective, so their colimit $B/I \to C/K$ is bijective. Finally, $q$ is a unit in $C$ because it is a unit in each $D_P$. $\square$

*Proof of the theorem.* Let $(D_j)$, $C$ and $K$ be as in the lemma, and let $n > 0$.

Each factor $R_k$ of $D_j$ is an absolutely integrally closed domain in which $q$ is a unit, so it is acyclic by axiom B5. A finite product of acyclic rings is acyclic: $\operatorname{Spec} \prod_k R_k$ is the disjoint union of the open and closed subschemes $\operatorname{Spec} R_k$, and the cohomology of a finite disjoint union is the product of the cohomology groups. So each $D_j$ is acyclic.

By axiom B1, the cohomology of $\mathrm{sp}(C)$ is the colimit of the cohomology of the $\mathrm{sp}(D_j)$. Each class $x \in H^n(\mathrm{sp}(C), \mathbb{Z}/q(i))$ comes from a class $y$ on some $\mathrm{sp}(D_j)$. Since $y = 0$, also $x = 0$. So $C$ is acyclic.

By axiom E1, the closed immersion $\mathrm{sp}(C/K) \to \mathrm{sp}(C)$ is an equivalence for $\mathbb{Z}/q(i)$, because $(C, K)$ is henselian and $q$ is a unit in $C$. So $C/K$ is acyclic. The isomorphism $B/I \cong C/K$ then shows that $B/I$ is acyclic. $\square$

**Remark 3.2.5.** Axiom E1 is the affine analogue of the proper base change theorem of O. Gabber, *Affine analog of the proper base change theorem*, Israel J. Math. 87 (1994). The theorem of this section uses it only through the henselian pair $(C, K)$ of the lemma.

**Remark 3.2.6 (Formalization).** The axioms of the theorem come as one record of hypotheses. The proof uses B1, B5 and E1 directly, and passes the whole record to the lemma on finite products. The lemma is proved from five statements: localization of absolutely integrally closed domains, splitting of monic polynomials, the idempotents of the third property, the passage to the colimit, and the construction of the diagram. The last step uses only the last two ([HensCut.lean](lean:Development/EtaleCohomology/EtaleSheaves/HensCut.lean#L39)), and the first three enter through the construction.
