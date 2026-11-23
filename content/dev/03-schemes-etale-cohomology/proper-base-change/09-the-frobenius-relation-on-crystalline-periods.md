---
title: The Frobenius relation on crystalline periods
decls:
  - UpperTheory.Ru.crystallineComparison.top
  - UpperTheory.Ru.crystallineComparison.final
  - UpperTheory.Ru.crystallineComparison.finAll_of
  - UpperTheory.Ru.crystallineComparison.finAll
  - UpperTheory.Ru.crystallineComparison.testFacts
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Frobenius relation on crystalline periods

In this section we move the congruence relation of [the previous section](/entry/w-zero/) from points to the étale cohomology of the generic fibre, tensored with the period ring $B_{\mathrm{cris}}$ of Fontaine. The result is a relation of Eichler-Shimura type between the crystalline Frobenius and the Hecke correspondences. The next section uses it to control the Frobenius of a Galois representation at a place above $\ell$.

### The statement

Let $\ell$ be a prime and let $K \subset \overline{\mathbb{Q}}_\ell$ be a finite extension of $\mathbb{Q}_\ell$, with ring of integers $\mathcal{O}_K$, uniformizer $\varpi$ and residue field of size $q = \ell^f$. Let $\mathcal{M} \to \operatorname{Spec} \mathcal{O}_K$ be projective and smooth, and put
$$V = H^j\bigl(\mathcal{M}_{\overline{K}}, \mathbb{Q}_\ell\bigr),$$
with its action of $G_K = \operatorname{Gal}(\overline{K}/K)$. Let $T_0, \dots, T_n$ be correspondences on $\mathcal{M}$ over $\mathcal{O}_K$ as in the previous section, and assume the point identity for them, with $q = \ell^f$.

**Definition 3.9.1 (Action of a correspondence).** A linear map $A : V \to V$ is the *action* of a correspondence $T = (Z, p, r, d)$ if for every smooth model $w : \mathcal{W} \to \mathcal{M}$ over $\mathcal{O}_K$ with sections $z_1, \dots, z_d$ of $T$ over $w$ that split $T$ where $\ell$ is a unit, we have
$$w^* (A v) = \sum_{i=1}^{d} (r \circ z_i)^* v \qquad (v \in V).$$

So $A$ is the map $p_* r^*$, computed on a cover where $p$ splits. Let $A_i$ be the action of $T_i$.

We write $\varphi$ for the Frobenius of $B_{\mathrm{cris}}$ and $G_K$ acts on $V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{cris}}$ diagonally (see the [Background](/learn/galois-representations/#period-rings)).

**Theorem 3.9.2 (Frobenius relation).** In this situation there is $N \geq 0$ such that for every $G_K$-invariant $x \in V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{cris}}$
$$\sum_{i=0}^{n} (-1)^i q^{\binom{i}{2}} \bigl(A_i \otimes \varphi^{f(n-i+N)}\bigr)(x) = 0.$$

Lean: `UpperTheory.Ru.crystallineComparison.finAll` (also `UpperTheory.Ru.crystallineComparison.finAll_of`, `UpperTheory.Ru.crystallineComparison.final` and `UpperTheory.Ru.crystallineComparison.top`, the forms with more hypotheses).

On $D_{\mathrm{cris}}(V) = (V \otimes B_{\mathrm{cris}})^{G_K}$ the linear Frobenius $\Phi = \varphi^f$ is bijective. So the theorem says that $\sum_i (-1)^i q^{\binom{i}{2}} A_i \Phi^{n-i}$ is zero on $D_{\mathrm{cris}}(V)$. This is the crystalline form of the Eichler-Shimura relation. For Siegel modular varieties, relations of this kind are in G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Chapter VII. The usual proof combines the crystalline comparison theorem of G. Faltings (*Crystalline cohomology and p-adic Galois representations*, 1989), which identifies $D_{\mathrm{cris}}(V)$ with the crystalline cohomology of the special fibre, with the congruence relation on the special fibre. We follow the same plan, with the test algebras of the previous section in place of the special fibre.

**Remark 3.9.3.** Let $t$ be the period of $\mathbb{Z}_\ell(1)$ in $A_{\mathrm{cris}}$. Let $C$ be a $\mathbb{Q}_\ell$-algebra with a ring map $c : A_{\mathrm{cris}} \to C$, a Frobenius and an action of $G_K$ compatible with $c$, such that $c(t)$ is a unit, each $x \in C$ has $c(t)^r x$ in the image of $c$ for some $r$, and the kernel of $c$ is the $t$-power torsion. Then $C = A_{\mathrm{cris}}[1/t]$, which is $B_{\mathrm{cris}}$ (J.-M. Fontaine, *Le corps des périodes p-adiques*, Astérisque 223, 1994). We state the results for $B_{\mathrm{cris}}$, and they hold for each such $C$.

### Two comparison inputs

The proof uses a map from étale cohomology to a cohomology of the functors of points of the previous section. For a functor $P$ on perfect algebras and a level $n \geq 0$, let $\mathrm{MH}^j_n(P)$ be the $j$-th cohomology of the category of elements of $P$, the pairs $(A, y)$ with $y \in P(A)$, with coefficients in the functor $(A, y) \mapsto A_{\mathrm{cris}}(A)$ at level $n$. These groups are $A_{\mathrm{cris}}$-modules, with a Frobenius $\varphi$ and pullbacks along natural maps. An *étale comparison family* gives, for each smooth model $\mathcal{M}$, maps
$$e_n : L \to \mathrm{MH}^j_n(P_{\mathcal{M}})$$
from an integral lattice $L \subset V$, natural in $\mathcal{M}$ and compatible with Frobenius. For $v_1, \dots, v_k \in L$ and $c_1, \dots, c_k \in A_{\mathrm{cris}}$ we write $e_n(v, c) = \sum_k c_k e_n(v_k)$.

The next theorem assumes two properties of $e$:

1. *Injectivity.* If $t^u e_n(v, c) = 0$ for all $n$, then $\sum_k v_k \otimes c(c_k) = 0$ in $V \otimes C$.
2. *Invariant classes come from the special fibre.* There are $m$, $N_1$, a map $g : \mathcal{O}_K \to \mathcal{O}_C^\flat/\varpi^\flat$ with $g(\varpi) = 0$, a Frobenius $F$ and a reduction $\rho$ as in the previous section, with this property. For each $G_K$-invariant $x = \sum_k v_k \otimes c(c_k)/c(t)^r$ there are $a, u$ and classes $y_n \in \mathrm{MH}^j_n(P_Q)$ with $\varphi^f y_n = F^* y_n$ and
$$\ell^a t^u \, e_n\bigl(v, \varphi^{f N_1}(c)\bigr) = t^{u + r} \rho^* y_n.$$

The second property is the place where the special fibre enters: the image of an invariant vector is, up to powers of $\ell$ and $t$, the pullback of a class $y$ on which the semilinear Frobenius $\varphi^f$ agrees with the geometric Frobenius $F^*$.

### Facts on test algebras

The proofs on test algebras use five properties of the ring $U(A)$. They give the charts in the proof of [Theorem 3.8.4](/entry/w-zero/), and the splittings of correspondences in the transfer argument below. For a test algebra $A$ we write $U = U(A)$, $U[1/\ell]$ for its localization at $\ell$, and $x^\sharp = \theta([x]) \in U$ for $x \in A$, where $[x]$ is the Teichmüller lift.

**Lemma 3.9.4 (Facts on test algebras).** Let $A$ be a test algebra and $U = U(A)$. Then:

1. $\ell$ is a nonzerodivisor in $U$;
2. each element of $U[1/\ell]$ that is integral over $U$ is the image of an element of $U$;
3. each étale surjective morphism of schemes $Y \to \operatorname{Spec} U[1/\ell]$ has a section;
4. each étale surjective morphism of schemes $Y \to \operatorname{Spec} U$ has a section;
5. for each idempotent $e$ of $U$ there is a unique idempotent $e_0$ of $A$ with $e_0^\sharp = e$.

Lean: `UpperTheory.Ru.crystallineComparison.testFacts`.

For a ring $S$ and $\varpi \in S$, we say that $S$ is *AIC* if every monic polynomial of positive degree over $S$ has a root, and that $S$ has *valuation type* for $\varpi$ if for all $a, b \in S$ with a power of $\varpi$ in $(a, b)$ there is an idempotent $e$ with $e a \in (b)$ and $(1 - e) b \in (a)$. A test algebra is AIC and has valuation type for $\varpi^\flat$. We say that $S$ is *local type* if for each $a \in S$ there is an idempotent $e$ with $e \in (a)$ and $1 - e \in (1 - a)$.

We take as given the following facts of commutative algebra and of untilting.

1. There is $\varpi \in U$ with $\varpi^\ell = \ell$ such that $U/\varpi^2$ is AIC and has valuation type for every element.
2. $\ell$ is a nonzerodivisor in $U$, $U$ is $\ell$-adically complete, and idempotents of $U$ come from unique idempotents of $A$ through $\sharp$.
3. Let $S$ be $\varpi$-adically complete with $\varpi$ a nonzerodivisor. If $S/\varpi^2$ is AIC and has valuation type for every element, then $S$ is AIC and has valuation type for $\varpi$. The proof passes to the quotients of $S$ by the ideals generated by the idempotents in a prime, shows a dichotomy there ($b \mid a$ or $a \mid b$ when a power of $\varpi$ is in $(a, b)$), and builds roots of monic polynomials by successive approximation.
4. If $S$ has valuation type for $\varpi$, then it has valuation type for $\varpi^\ell$; and $S$ is $\varpi$-adically complete if and only if it is $\varpi^\ell$-adically complete.
5. If $S$ has valuation type for $\ell$, then $S$ and $S[1/\ell]$ are local type, and if $S$ is also AIC, then so is $S[1/\ell]$. In this case $S$ is integrally closed in $S[1/\ell]$ if $\ell$ is a nonzerodivisor.
6. If $S$ is AIC and local type, then every étale surjective morphism $Y \to \operatorname{Spec} S$ has a section. The proof finds a section at each maximal ideal and glues these sections along idempotents.

*Proof.* Fact 2 gives 1 and 5. Let $\varpi$ be as in fact 1. By fact 2 and fact 4, $U$ is $\varpi$-adically complete. Since $\varpi^{\ell - 1} \cdot \varpi = \ell$ is a nonzerodivisor, so is $\varpi$. Fact 3 now says that $U$ is AIC and has valuation type for $\varpi$, and fact 4 says that $U$ has valuation type for $\varpi^\ell = \ell$. By fact 5, $U$ and $U[1/\ell]$ are local type, $U[1/\ell]$ is AIC, and $U$ is integrally closed in $U[1/\ell]$; this is 2. Fact 6 applied to $U[1/\ell]$ and to $U$ gives 3 and 4. $\square$

### The proof

**Theorem 3.9.5 (Frobenius relation from the comparison inputs).** Let $K$ be as above, except that $[K : \mathbb{Q}_\ell]$ may be infinite and $f > 0$ is any integer, with $q = \ell^f$ not tied to the residue field. Let $\mathcal{M}$ be smooth and quasi-compact over $\mathcal{O}_K$, with each finite set of points in one affine open. Assume the point identity, let $A_i$ be the action of $T_i$, and let $e$ be an étale comparison family with the two properties. Then the conclusion of the Frobenius relation holds.

Lean: `UpperTheory.Ru.crystallineComparison.top`.

*Proof.* Take $m$, $N_1$, $g$, $F$ and $\rho$ from the second property, and a cover $\pi : W \to \mathcal{M}$ with sections $s_{i,k}$ that split the $T_i$. [Theorem 3.8.4](/entry/w-zero/) gives $N_0$ and the relation
$$\sum_{i} (-1)^i q^{\binom{i}{2}} \sum_k F^{\,n-i+N_0} \circ \rho \circ (r_i \circ s_{i,k})_* = 0$$
on test algebras. We put $N = N_0 + N_1$.

Let $x$ be $G_K$-invariant. Since $L$ spans $V$ and $C = A_{\mathrm{cris}}[1/t]$, we can write $x = \sum_k v_k \otimes c(c_k)/c(t)^r$ with $v_k \in L$. The second property gives $a$, $u$ and the classes $y_n$.

Relations on test algebras pass to $\mathrm{MH}$, because the cohomology of the category of elements can be computed on test algebras: if a relation $\sum_t a_t\, u_t \circ \rho \circ F^{k_t} = 0$ holds on test algebras and $\varphi^f y = F^* y$, then $\sum_t a_t\, u_t^* \varphi^{f k_t} \rho^* y = 0$. With the relation above, this gives
$$\sum_i (-1)^i q^{\binom{i}{2}} \sum_k (r_i \circ s_{i,k})^* \varphi^{f(n-i+N_0)} \rho^* y_n = 0.$$

By the definition of the action, $\pi^* A_i v = \sum_k (r_i s_{i,k})^* v$. On the lattice $L$ this identity holds up to a power $\ell^b$, which clears the denominators of $A_i$ on $L$. We combine this with the second property and move $\varphi$ through the sums, using $\varphi(t) = \ell t$. The result is a relation $t^{u'} \pi^* e_n(w, c') = 0$ for all $n$, for the vector $\kappa$ times the left side of the theorem, with $\kappa = |\prod_i S_{d_i}| \cdot \ell^{a'}$ for some $a'$. A transfer argument removes $\pi^*$: the symmetric groups $S_{d_i}$ permute the sections $s_{i,k}$, and a class that dies on $W$ is killed by $|\prod_i S_{d_i}|$.

The first property now says that $\kappa$ times the left side of the theorem is $0$ in $V \otimes C$. Since $\kappa \neq 0$ and $V \otimes C$ is a $\mathbb{Q}_\ell$-vector space, the left side is $0$. $\square$

**Corollary 3.9.6 (Final form).** Assume that $K$ is finite over $\mathbb{Q}_\ell$, that $\mathcal{M}$ is projective and smooth over $\mathcal{O}_K$, and that the residue datum of $K$ (below) satisfies $x^q = x$. Assume the comparison input (below) for this datum. Then the conclusion of the Frobenius relation holds.

Lean: `UpperTheory.Ru.crystallineComparison.final`.

*Proof.* A projective map is proper, so it is quasi-compact, and the points of a projective scheme over a local ring satisfy the condition on finite sets. The comparison input provides an étale comparison family $e$ and the data of the two properties. An injective ring map from $C$ to the period ring of the input, compatible with $G_K$, gives the first property. The second property comes from the Teichmüller congruence of the input together with $x^q = x$ on the residue field. The theorem above then applies. $\square$

**Definition 3.9.7 (Comparison input).** For $K$, a residue datum and $f > 0$, the *comparison input* consists of the basic facts on the period ring, the étale comparison maps $e$ for all smooth models with their laws, maps from étale cohomology to $\mathrm{MH}$ and back, an integer $N$ divisible by $f$ with a Teichmüller congruence for the residue datum at level $N$, and the two properties above at each smooth model and each degree $j$.

A *residue datum* for $K$ is a perfect field $k$ of characteristic $\ell$, a surjective ring map $\mathcal{O}_K \to k$, and a ring map $s : k \to \mathcal{O}_C^\flat$ such that for each $x \in \mathcal{O}_K$ the untilt of $s$ applied to the residue of $x$ is at distance less than $1$ from $x$.

*Proof of the Frobenius relation.* First, $K$ has a residue datum. Let $k$ be the residue field of $\mathcal{O}_K$, a finite field. The ring $\mathcal{O}_C^\flat$ is complete with residue field $\overline{\mathbb{F}}_\ell$, so an embedding $k \to \overline{\mathbb{F}}_\ell$ lifts by Hensel's lemma to a ring map $s : k \to \mathcal{O}_C^\flat$. The untilt of $s(\bar{x})$ is the Teichmüller lift of $\bar{x}$, which is congruent to $x$ modulo the maximal ideal of $\mathcal{O}_C$. Now let $(k, \mathcal{O}_K \to k, s)$ be a residue datum. The kernel of the surjective map $\mathcal{O}_K \to k$ is a maximal ideal, so it is the maximal ideal of the local ring $\mathcal{O}_K$, and $k$ is the residue field. So $|k| = q$, and $x^q = x$ for all $x \in k$ because $k$ is a finite field with $q$ elements. The comparison input holds for each residue datum and each $f > 0$. This is the crystalline comparison theorem in the form that we need (G. Faltings, *Crystalline cohomology and p-adic Galois representations*, 1989), and we take it as given here. So the final form applies. $\square$

**Remark 3.9.8 (Formalization).** The ring $B_{\mathrm{cris}}$ is a period datum $(C, c)$ as in the first remark, and the statements quantify over all period data; $A_{\mathrm{cris}}$, $\mathrm{MH}$, the lattice $L$, the comparison family and the comparison input are definitions that we describe in words. `UpperTheory.Ru.crystallineComparison.top` asks neither $[K : \mathbb{Q}_\ell] < \infty$ nor a link between $q$ and the residue field; `final` asks both. `finAll_of` assumes the comparison input for every residue datum but uses it for one ([FinAllOf.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/FinAllOf.lean#L11)), and `finAll` supplies it by `cIn`. The condition $g(x)^q = g(x)$ goes to [Theorem 3.8.4](/entry/w-zero/), which does not use it. The names `top`, `final` and `finAll` do not describe the statements, and two files are named after helpers ([QuasiCompactOfProj.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/QuasiCompactOfProj.lean#L26), and the file of `phiH_iter_smul`). The cover `wEx`, `wTrans`, `avgMH`, `siteAnn`, `levZero`, `hecke_correspondence_product`, `exists_crystalline_lattice_expansion`, `crystalline_expansion_relation_of_scaled_endomorphisms`, and for the final form `etMap`, `ePin`, `pbIota`, `injOf`, `absInvOf`, `pbInv`, `resEx` and `cIn` were checked from their statements. In the facts on test algebras, the six inputs are lemmas proved elsewhere in the development, under the prefix `RL`, and the reasons that we give for them are summaries; items 3 and 4 of the lemma hold for arbitrary schemes $Y$, not only quasi-compact ones ([TestFacts.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/TestFacts.lean#L89)).
