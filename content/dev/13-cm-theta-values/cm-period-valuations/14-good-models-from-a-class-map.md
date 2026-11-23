---
title: Good models from a class map
decls:
  - GlobalTheory.T.cmLattice_good_model_unramified
  - GlobalTheory.ArtinClassCM.good_model
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Good models from a class map

Sections 6 and 13 assumed the CM good model condition of Section 13: every lattice with complex multiplication by $d$ has a good model at every prime $l \ge 5$ with $l \nmid d$. This section proves it from two inputs on Galois groups of number fields: a class map, which is the unramified part of Artin reciprocity, and a form of the Chebotarev density theorem. The proof is the classical one. The singular modulus $j(L)$ is an algebraic integer, and the Kronecker congruence shows that every inertia element at $l$ fixes it, so $j(L)$ is unramified at $l$. A curve with an integral unramified $j$-invariant then has a good model. The result is used by [the theorem on good models from global Artin reciprocity](/entry/cm-good-model-of-global-artin-reciprocity/) of Volume 14, which supplies both inputs, and through it by [the service row from Artin reciprocity](/entry/serv-h-row-of-artin/).

### Inertia and Frobenius on valuation rings

Let $E$ be a number field with ring of integers $\mathcal{O}_E$, and $\Omega$ an algebraic closure of $E$. Write $G_E = \mathrm{Gal}(\Omega/E)$ with its Krull topology. We work with valuation subrings $A \subset \Omega$ in place of primes of $\Omega$; we write $\mathfrak{m}_A$ for the maximal ideal of $A$, that is, the set of nonunits of $A$.

**Definition 5.14.1 (Lies above).** A valuation subring $A$ of $\Omega$ *lies above* a nonzero prime $v$ of $\mathcal{O}_E$ if for every $x \in \mathcal{O}_E$ we have $x \in \mathfrak{m}_A$ if and only if $x \in v$.

**Definition 5.14.2 (Inertia element).** Let $A$ be a valuation subring of $\Omega$. An element $g \in G_E$ is an *inertia element at* $A$ if $g(A) = A$ and $g(x) - x \in \mathfrak{m}_A$ for every $x \in A$.

**Definition 5.14.3 (Arithmetic Frobenius).** Let $A$ lie above $v$, and let $N(v) = |\mathcal{O}_E / v|$. An element $\varphi \in G_E$ is an *arithmetic Frobenius at* $A$ over $v$ if $\varphi(A) = A$ and $\varphi(x) - x^{N(v)} \in \mathfrak{m}_A$ for every $x \in A$.

So the inertia elements at $A$ are the elements of the decomposition group of $A$ that act trivially on the residue field, and an arithmetic Frobenius acts on the residue field as $x \mapsto x^{N(v)}$. These are the usual notions for the place of $\Omega$ defined by $A$.

**Definition 5.14.4 (Class map).** A *class map* for $(E, \Omega)$ is a group homomorphism $\mathrm{art} : G_E \to \mathrm{Cl}(\mathcal{O}_E)$ to the ideal class group such that:
1. the kernel of $\mathrm{art}$ is open in $G_E$;
2. $\mathrm{art}(g) = 1$ for every valuation subring $A$ of $\Omega$ and every inertia element $g$ at $A$;
3. if $A$ lies above $v$ and $\varphi$ is an arithmetic Frobenius at $A$ over $v$, then $\mathrm{art}(\varphi) = [v]$.

The fixed field of the kernel is then a finite extension of $E$, unramified at all finite places, on which the Frobenius at $v$ has image the class of $v$. This is the Artin map of the Hilbert class field ([global class field theory](/learn/class-field-theory/#global-class-field-theory), [[Artin reciprocity|7938EKMMVR]]).

**Definition 5.14.5 (Chebotarev condition).** The *Chebotarev condition* says the following. Let $E$ be a number field with algebraic closure $\Omega$, let $S$ be a finite set of nonzero primes of $\mathcal{O}_E$, and let $H \subseteq G_E$ be an open normal subgroup that contains every inertia element at every valuation subring $A$ that lies above a prime $v \notin S$. Then for every $\sigma \in G_E$ there are a valuation subring $A$, a prime $v$ and an element $\varphi \in G_E$ such that $A$ lies above $v$, $v \notin S$, $N(v)$ is a prime number, $\varphi$ is an arithmetic Frobenius at $A$ over $v$, and $\sigma^{-1}\varphi \in H$.

The fixed field of $H$ is a finite Galois extension of $E$ unramified outside $S$, and the condition says that the class of $\sigma$ in its Galois group is the Frobenius class of a prime of degree $1$ outside $S$. This follows from the Chebotarev density theorem, because the primes of degree $1$ have Dirichlet density $1$.

### Good models

Recall from Section 13 the number $\omega_d = (1 + i\sqrt{d})/2$, the field $K_d = \mathbb{Q}(\sqrt{-d}) \subset \mathbb{C}$, lattices $L$ with complex multiplication by $d$, good models at $(l, \iota)$, and the CM good model condition. Write $j(L) = 1728\, g_2(L)^3 / (g_2(L)^3 - 27 g_3(L)^2)$ for the $j$-invariant of $L$, as in Section 10, and $\Omega_d$ for the algebraic closure of $K_d$ in $\mathbb{C}$.

**Theorem 5.14.6 (Good models from a class map).** Assume that every number field $E$ with an algebraic closure $\Omega$ has a class map, and assume the Chebotarev condition. Then the CM good model condition holds.

Lean: `GlobalTheory.ArtinClassCM.good_model` (also `GlobalTheory.T.cmLattice_good_model_unramified`, a second name)

*Proof.* We use three facts on singular moduli.

1. *Integrality.* For every $d$ and $L$ as above and every prime $l$ and every isomorphism $\iota : \mathbb{C} \to \mathbb{C}_l$, we have $|\iota(j(L))| \le 1$. This is the integrality of singular moduli of Section 10: $j(L)$ is an algebraic integer.
2. *Reduction.* If, in addition to 1, the element $\iota(j(L))$ lies in the completion of $\mathbb{Q}_l^{\mathrm{ur}}$ for every $l \ge 5$ with $l \nmid d$ and every $\iota$, then the CM good model condition holds. This is [the theorem on good reduction from an integral unramified $j$-invariant](/entry/good-reduction-of-integral-unramified/); its proof is not unfolded here.
3. *Kronecker congruence.* Let $A$ be a valuation subring of $\Omega_d$ that lies above a prime $v$ of $\mathcal{O}_{K_d}$ with $N(v)$ prime, and assume that the class of $v$ in $\mathrm{Cl}(\mathcal{O}_{K_d})$ is trivial. Let $x \in \Omega_d$ with $x = j(L)$. Then $x^{N(v)} - x \in \mathfrak{m}_A$.

By 2 we must show that $\iota(j(L))$ is unramified at $l$. Since $j(L)$ is an algebraic integer, $j(L) = x$ for an element $x \in \Omega_d$ that is integral over $\mathbb{Z}$. Let $A_\iota$ be the valuation subring of $\Omega_d$ pulled back from the ring of integers of $\mathbb{C}_l$ by $\iota$. For $l \ne 2$ and $l \nmid d$, an element $x \in \Omega_d$ that is fixed by every inertia element at $A_\iota$ in $\mathrm{Gal}(\Omega_d/K_d)$ has $\iota(x)$ in the completion of $\mathbb{Q}_l^{\mathrm{ur}}$: the fixed field of the inertia group is unramified over the completion of $K_d$, which is itself unramified over $\mathbb{Q}_l$. Here $l \ge 5$, so $l \ne 2$. It remains to show: *every inertia element $\sigma$ at a valuation subring $B$ of $\Omega_d$ fixes $x$.*

Let $\mathrm{art}$ be a class map for $(K_d, \Omega_d)$. Let $P \in \mathbb{Z}[X]$ be monic with $P(x) = 0$, and let $R \subset \Omega_d$ be the finite set of roots of $P$. All elements of $R$ are algebraic integers. So there is an integer $n \ne 0$ with this property: if $r \ne r'$ are in $R$ and $r - r' \in \mathfrak{m}_A$ for a valuation subring $A$, then $n \in \mathfrak{m}_A$. (For example $n = \prod (r - r')$ over the ordered pairs $r \ne r'$ in $R$: it is a nonzero algebraic integer fixed by $G_{\mathbb{Q}}$, so a nonzero integer, and every valuation subring contains the algebraic integers, so $r - r' \in \mathfrak{m}_A$ gives $n \in \mathfrak{m}_A$.) Let $S$ be the set of primes $v$ of $\mathcal{O}_{K_d}$ with $n \in v$. It is finite. If $A$ lies above $v \notin S$, then $n \notin \mathfrak{m}_A$, so two roots in $R$ that are congruent modulo $\mathfrak{m}_A$ are equal.

Let $H = \ker(\mathrm{art}) \cap \mathrm{Stab}(R)$, where $\mathrm{Stab}(R)$ is the subgroup of elements that fix each element of $R$. Both groups are open and normal, so $H$ is open and normal. Let $g$ be an inertia element at $A$, with $A$ above $v \notin S$. Then $\mathrm{art}(g) = 1$ by property 2 of a class map. For $r \in R$, the element $g(r)$ is again in $R$, and $g(r) - r \in \mathfrak{m}_A$ since $r \in A$. So $g(r) = r$, and $g \in H$. Thus $H$ satisfies the hypothesis of the Chebotarev condition. Apply it to $\sigma$: we get $A$ above $v \notin S$ with $N(v)$ prime and an arithmetic Frobenius $\varphi$ at $A$ over $v$ with $\sigma^{-1}\varphi \in H$.

Now $\mathrm{art}(\sigma) = 1$, since $\sigma$ is an inertia element, and $\mathrm{art}(\sigma^{-1}\varphi) = 1$. So $\mathrm{art}(\varphi) = 1$. By property 3, $[v] = \mathrm{art}(\varphi) = 1$, so $v$ is principal. The Kronecker congruence gives $x^{N(v)} - x \in \mathfrak{m}_A$, and the Frobenius property gives $\varphi(x) - x^{N(v)} \in \mathfrak{m}_A$. Hence $\varphi(x) - x \in \mathfrak{m}_A$. Both $\varphi(x)$ and $x$ are in $R$ and $v \notin S$, so $\varphi(x) = x$. Finally $\sigma^{-1}\varphi$ fixes every root of $P$, so $\sigma^{-1}(x) = \sigma^{-1}(\varphi(x)) = x$, and $\sigma(x) = x$. $\square$

The proof uses the class map only at the field $K_d$, and only through the triviality of the class of $v$. This is the step "Frobenius of a principal prime of degree $1$ fixes $j(L)$ modulo $A$", which in the classical theory comes from the main theorem of complex multiplication: $K_d(j(L))$ is the Hilbert class field of $K_d$.

**Remark 5.14.7 (Formalization).** Several facts about the Lean code:
1. `GlobalTheory.T.cmLattice_good_model_unramified` is a second name of `good_model`, proved by `first | exact @… | …` under `maxHeartbeats 1000000` (CmLatticeGoodModelUnramifiedStatement.lean:7).
2. The theorem is named after Artin reciprocity, but its hypothesis is the class map above, a homomorphism from $G_E$ to the class group, together with the Chebotarev condition `ChebOmSt` (ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/ModChebOm.lean:10). It is not idelic Artin reciprocity. The only caller in the chapter outline, `GlobalTheory.Corev.CmTwoClosing.cmGoodModel_of_globalArtinReciprocity`, supplies the class map with `GlobalTheory.T.exists_idealClass_artinSymbol_of_globalArtin` and the Chebotarev condition with the theorem `GlobalTheory.T.chebotarev_degreeOne_valuationSubrings` (DecoratedLatticeProofs/CmGoodModelOfGlobalArtinReciprocity.lean:11). Neither of the two is in the chapter outline.
3. The integrality fact 1 is the theorem `jInt`, proved with no hypothesis (ModJInt.lean:43). So the two inputs are used only for the unramified part `JUnram` (Interface.lean:13). The reduction fact 2 is `goodReduction_of_integral_unramified` (RedStatus.lean:13), and the Kronecker congruence 3 is `frobCong` (ModFrobCong.lean:32); their proofs are not unfolded here.
4. The unramified field is `MaximalUnramifiedExtension l`, the topological closure of the field generated by the roots of unity of order prime to $l$ (Formalism/LocalToGlobal/TorsionIntegrality/CMGoodModels/Statement.lean:14). So it is the completion of $\mathbb{Q}_l^{\mathrm{ur}}$, not $\mathbb{Q}_l^{\mathrm{ur}}$ itself.
5. The step from inertia invariance to the unramified field is `inertKur`, which needs $l \ne 2$; the proof gets it from $5 \le l$ by `omega` (CmLatticeGoodModelUnramified.lean:69). The main step of the proof is the lemma `inertia_fixes` (same file, line 10), with the integer $n$ from `sepInt` (ModSepInt.lean:35) and $H$ = `art.ker ⊓ fixJStab`.
