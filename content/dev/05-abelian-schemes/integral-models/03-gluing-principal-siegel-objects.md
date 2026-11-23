---
title: Gluing principal Siegel objects
decls:
  - GlobalTheory.ArtinGlue.exists_principal_glue
  - GlobalTheory.T.exists_principalSiegelObject_glue_artinFibreProduct
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gluing principal Siegel objects

This section extends the gluing of the previous section from abelian schemes to Siegel objects with a principal polarization. Let $P = R_1 \times_{R_0} R_2$ be an Artinian fibre product. Two principal Siegel objects over $R_1$ and $R_2$ that come from one Siegel object over $R_0$ glue to a principal Siegel object over $P$. In the language of Schlessinger ("Functors of Artin rings", Trans. Amer. Math. Soc. 130 (1968), 208 to 222, §2), this is the surjectivity part of his condition (H1) for the functor of principal Siegel objects. The abelian scheme comes from the previous section. The line bundle comes from the patching of Milnor (*Introduction to Algebraic K-Theory*, Annals of Math. Studies 72, §2), and the level structure comes from the fact that $\operatorname{Spec} P$ is a pushout of $\operatorname{Spec} R_1$ and $\operatorname{Spec} R_2$. We keep the notation of the first section: $M \geq 3$ is odd, $B_M = \mathbb{Z}[\zeta_M, 1/M]$, and Siegel objects $(A, P, \lambda)$ have genus $h$ and level $M$.

### Maps and principal objects

**Definition 8.3.1 (Map of Siegel objects).** Let $c' = (A', P', \lambda')$ be a Siegel object over $s' : S' \to \operatorname{Spec} B_M$, let $c = (A, P, \lambda)$ be a Siegel object over $s : S \to \operatorname{Spec} B_M$, and let $f : S' \to S$ be a map of schemes. A *map* $c' \to c$ over $f$ is a group pullback $\varphi : A' \to A$ along $f$ such that $P'$ is isomorphic to $(\varphi \times \varphi)^* P$ and $\varphi \lambda'(a) = \lambda(a) f$ for every $a \in \mathbb{Z}^{2h}$.

Here $\lambda(a)$ is a section of $A \to S$, and $\varphi \times \varphi$ is the map $A' \times_{S'} A' \to A \times_S A$. If there is a map $c' \to c$ over $f$, we also say that $c'$ is a *pullback* of $c$ along $f$.

**Definition 8.3.2 (Principal Siegel object).** A Siegel object $(A, P, \lambda)$ over $S$ is *principal* if $\Delta^* P$ is relatively ample over $S$ and the following holds. For every scheme $T$ over $S$ and every $x \in A(T)$, if the pullback of $P$ along the map $A \times_S T \to A \times_S A$, $(a, t) \mapsto (x(t), a)$, is trivial, then $x = 0$.

So a principal Siegel object is a Siegel object with kernel killed by $1$, in the sense of the first section. The pullback condition says that $x$ lies in the kernel of the polarization $A \to A^\vee$ given by $P$. For [line bundles and the Picard group](/learn/commutative-algebra/#picard-groups) we write $\operatorname{Pic}(X)$, and we call a line bundle trivial if it has a nowhere vanishing global section. See also [line bundles and divisors](/learn/geometry/#line-bundles-and-divisors).

### Inputs

In the rest of the section we fix an Artinian fibre product $P = R_1 \times_{R_0} R_2$ with maps $f_1, f_2, g_1, g_2$ as in the previous section. We use the following five results.

1. (Patching of line bundles.) Let $X$ be flat over $P$, let $X_1 = X \times_P R_1$ and $X_2 = X \times_P R_2$ with maps $j_1$, $j_2$ to $X$, and let $X_0 = X_1 \times_{R_1} R_0$ with maps $i_1 : X_0 \to X_1$ and $i_2 : X_0 \to X_2$ over $g_1$ and $g_2$ such that $j_1 i_1 = j_2 i_2$. Let $L_1$ and $L_2$ be line bundles on $X_1$ and $X_2$ with $i_1^* L_1 \cong i_2^* L_2$. Then there is a line bundle $L$ on $X$ with $j_1^* L \cong L_1$ and $j_2^* L \cong L_2$.
2. (Injectivity on the Picard group.) Let $A$ be an abelian scheme over $P$ with base changes $A_1$ and $A_2$ to $R_1$ and $R_2$. If a class in $\operatorname{Pic}(A)$ has trivial pullback to $A_1$ and to $A_2$, then it is zero.
3. (Field points.) Every map $\operatorname{Spec} k \to \operatorname{Spec} P$ from the spectrum of a field factors through $\operatorname{Spec} R_1$ or through $\operatorname{Spec} R_2$.
4. (Principal from one side.) Suppose that $R_1 \neq 0$. Let $c$ be a Siegel object over $P$ and $c_1$ a principal Siegel object over $R_1$ with a map $c_1 \to c$ over $f_1$. Then $c$ is principal.
5. (Flat pushout.) Every flat scheme $Y$ over $P$ is the pushout of $Y \times_P R_1$ and $Y \times_P R_2$ along $Y \times_P R_0$.

The idea of result 2 is the exact sequence of Milnor for units and Picard groups. The global functions on the base change of $A$ to $R_\nu$ are $R_\nu$, and every unit of $R_0$ lifts to a unit of $R_1$ since $\ker g_1$ is nilpotent. The idea of result 4 is that relative ampleness and the triviality of the kernel can be checked on the closed fibre, and the closed point of $\operatorname{Spec} P$ lies in the image of $\operatorname{Spec} R_1$.

**Lemma 8.3.3 (The spectrum is a pushout).** The square of schemes with $\operatorname{Spec} g_1$, $\operatorname{Spec} g_2$, $\operatorname{Spec} f_1$ and $\operatorname{Spec} f_2$ is a pushout.

Lean: `GlobalTheory.ArtinGlue.spec_isPushout`.

*Proof.* Apply result 5 to $Y = \operatorname{Spec} P$, which is flat over $P$. $\square$

**Lemma 8.3.4 (Transfer of the geometric condition).** Let $c' = (A', P', \lambda')$ be a Siegel object over $S'$, let $A$ be a commutative group scheme over $S$ with a line bundle $P$ on $A \times_S A$ and maps $\lambda(a)$ from $S$ to $A$, and let $\varphi : A' \to A$ be a group pullback along $f : S' \to S$ with $\Delta^* P' \cong \varphi^* \Delta^* P$ and $\varphi \lambda'(a) = \lambda(a) f$. Let $x$ be a geometric point of $S$ that factors as $x = f y$ with $y$ a geometric point of $S'$. Then the geometric conditions of a symplectic level $M$ structure hold for $\lambda$ at $x$.

Lean: `GlobalTheory.ArtinGlue.geom_transfer`.

*Proof.* Let $k$ be the algebraically closed field of $x$. The group pullback gives an injective group homomorphism $\sigma : A_x(k) \to A'_y(k)$, and since $A'_y = A_x$, it is bijective. It carries $\lambda_x(a)$ to $\lambda'_y(a)$. So $\lambda_x(a) = 0$ if and only if $a \in M\mathbb{Z}^{2h}$, and every $M$-torsion point of $A_x$ is a $\lambda_x(a)$, since both statements hold for $\lambda'_y$. The Weil pairing of $\Delta^* P$ at $x$ agrees with the Weil pairing of $\Delta^* P'$ at $y$, since $\Delta^* P' \cong \varphi^* \Delta^* P$ and the Weil pairing is compatible with a group pullback. So $e_M(\lambda_x(a), \lambda_x(b)) = \beta(\zeta_M)^{2\langle a, b \rangle}$. $\square$

### The gluing theorem

**Theorem 8.3.5 (Gluing principal Siegel objects).** Let $h \geq 0$, let $M \geq 3$ be odd, let $P = R_1 \times_{R_0} R_2$ be an Artinian fibre product and let $\beta : B_M \to P$ be a ring map. Let $c_1$ and $c_2$ be principal Siegel objects over $R_1$ and $R_2$, with the structure maps through $\beta f_1$ and $\beta f_2$. Suppose that there is a Siegel object $c_0$ over $R_0$ with maps $c_0 \to c_1$ over $g_1$ and $c_0 \to c_2$ over $g_2$. Then there is a principal Siegel object $c$ over $P$ with maps $c_1 \to c$ over $f_1$ and $c_2 \to c$ over $f_2$.

Lean: `GlobalTheory.ArtinGlue.exists_principal_glue` (also `GlobalTheory.T.exists_principalSiegelObject_glue_artinFibreProduct`).

*Proof.* Write $c_\nu = (A_\nu, P_\nu, \lambda_\nu)$ for $\nu = 0, 1, 2$, and let $\psi_1 : A_0 \to A_1$ and $\psi_2 : A_0 \to A_2$ be the group pullbacks of the two maps.

Step 1 (abelian scheme). The [theorem on gluing abelian schemes](/entry/glue-ab-main/) gives an abelian scheme $A$ over $P$ and group pullbacks $\varphi_1 : A_1 \to A$ and $\varphi_2 : A_2 \to A$ with $\varphi_1 \psi_1 = \varphi_2 \psi_2$. Then $A \times_P A$ is an abelian scheme, so it is flat over $P$, and $\varphi_1 \times \varphi_1$ and $\varphi_2 \times \varphi_2$ identify $A_1 \times A_1$ and $A_2 \times A_2$ with its base changes.

Step 2 (line bundle). On $A_0 \times A_0$ we have $(\psi_1 \times \psi_1)^* P_1 \cong P_0 \cong (\psi_2 \times \psi_2)^* P_2$. Result 1 for $X = A \times_P A$ gives a line bundle $L$ on $A \times_P A$ with $(\varphi_\nu \times \varphi_\nu)^* L \cong P_\nu$ for $\nu = 1, 2$.

Step 3 (rigidity and symmetry). Let $e : A \to A \times_P A$ be the map $a \mapsto (0, a)$. Its base change to $R_\nu$ is the same map for $A_\nu$, and $P_\nu$ is trivial on $0 \times A_\nu$. So $e^* L$ has trivial pullbacks to $A_1$ and $A_2$, and result 2 shows that $e^* L$ is trivial. The same holds for $a \mapsto (a, 0)$. Let $\tau$ be the swap of the two factors. The class of $L$ minus the class of $\tau^* L$ in $\operatorname{Pic}(A \times_P A)$ has zero pullbacks, since $P_1$ and $P_2$ are symmetric. Result 2 for the abelian scheme $A \times_P A$ shows that $L \cong \tau^* L$.

Step 4 (level structure). For $a \in \mathbb{Z}^{2h}$ the maps $\varphi_1 \lambda_1(a) : \operatorname{Spec} R_1 \to A$ and $\varphi_2 \lambda_2(a) : \operatorname{Spec} R_2 \to A$ agree on $\operatorname{Spec} R_0$, since both are $\varphi_1 \psi_1 \lambda_0(a)$ there. The first lemma gives a unique map $\lambda(a) : \operatorname{Spec} P \to A$ with $\lambda(a) f_\nu = \varphi_\nu \lambda_\nu(a)$, and it is a section. Two sections of $A$ over $P$ with the same pullbacks to $R_1$ and $R_2$ are equal by the same lemma. Since $\lambda_1$ and $\lambda_2$ are additive and killed by $M$, so is $\lambda$.

Step 5 (geometric condition). By result 3, every geometric point of $\operatorname{Spec} P$ factors through $\operatorname{Spec} R_1$ or $\operatorname{Spec} R_2$. The second lemma, applied to $c_1$ or to $c_2$, gives the geometric conditions. So $c = (A, L, \lambda)$ is a Siegel object over $P$, and by construction $\varphi_1$ and $\varphi_2$ are maps $c_1 \to c$ and $c_2 \to c$.

Step 6 (principal). By result 3, the residue field point of $P$ factors through $\operatorname{Spec} R_1$ or through $\operatorname{Spec} R_2$, and that ring is not zero. In the first case result 4 shows that $c$ is principal, since $c_1$ is principal. In the second case apply result 4 with the indices exchanged. $\square$

We did not show directly that $\Delta^* L$ is relatively ample. It follows in step 6 from result 4. The object $c_0$ need not be principal, and the genus $h$ can be $0$.

**Remark 8.3.6 (Formalization).** The names `GlobalTheory.ArtinGlue.lem_ab`, `lem_lb`, `lem_triv`, `lem_pt` and `lem_princ` are second names for results that are proved elsewhere: [ExistsPrincipalSiegelObjectGlueArtinFibreProduct.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPrincipalSiegelObjectGlueArtinFibreProduct.lean#L31). The field point result 3 has no local or Artinian hypothesis on $P$: [ExistsPrincipalSiegelObjectGlueArtinFibreProduct.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPrincipalSiegelObjectGlueArtinFibreProduct.lean#L37). Relative ampleness of the glued object is never shown directly; principality comes from result 4 at the end: [ExistsPrincipalSiegelObjectGlueArtinFibreProduct.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPrincipalSiegelObjectGlueArtinFibreProduct.lean#L189). A map of Siegel objects does not ask that $s' = s f$; this compatibility of the bases is carried separately in the types of the objects: [Clauses.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/Clauses.lean#L50). Principality states the triviality of the kernel through a line bundle with a global generator: [Clauses.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/Clauses.lean#L41). Line bundles are Čech data with transition units, and the Picard group is a group of classes of such data. The statement wrapper raises the heartbeat limit and calls the proof through a `first` tactic: [ExistsPrincipalSiegelObjectGlueArtinFibreProductStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPrincipalSiegelObjectGlueArtinFibreProductStatement.lean#L10). We read the statements of results 1 to 5, not their proofs.
