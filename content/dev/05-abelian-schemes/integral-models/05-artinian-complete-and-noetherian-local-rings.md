---
title: Artinian, complete and noetherian local rings
decls:
  - GlobalTheory.SiegelArtin.main
  - GlobalTheory.T.siegel_point_lifts_to_artinian
  - GlobalTheory.SFamCompl.classified_of_complete
  - GlobalTheory.T.siegelFamily_classifies_complete_noetherian_local
  - GlobalTheory.SiegelFamLocal.exists_point_of_principal
  - GlobalTheory.T.siegelFamily_classifies_noetherian_local
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Artinian, complete and noetherian local rings

Let $F = (X, s, u)$ be a Siegel family of genus $h \geq 1$ and odd level $M \geq 3$, as in the previous section. This section shows that $F$ classifies every principal Siegel object over the spectrum of a noetherian local ring. There are three steps. Over a local Artinian ring we use induction on the length, with the small extension theorem as the induction step. Over a complete noetherian local ring $R$ we pass to the limit over the Artinian rings $R/\mathfrak{m}^{e+1}$, and we use the rigidity of level structures and Grothendieck's existence theorem to compare the given object with the pullback of $u$. Over a noetherian local ring we use faithfully flat descent along the [completion](/learn/commutative-algebra/#completion). This is the usual way from formal moduli to moduli over local rings; see Schlessinger ("Functors of Artin rings", Trans. Amer. Math. Soc. 130 (1968), 208 to 222) and the [deformation functors](/learn/deformations-patching/#deformation-functors) of Volume 1.

### Artinian local rings

We use the following results. We state them as we use them.

1. (Fields.) $F$ classifies every principal Siegel object over every map $\operatorname{Spec} k \to \operatorname{Spec} B_M$, where $k$ is a field.
2. (Pullbacks.) A pullback of a principal Siegel object is principal. This is result 1 of the previous section.

**Lemma 8.5.1 (Socle element).** Let $C$ be a local Artinian ring whose maximal ideal $\mathfrak{m}$ is not zero. Then there is a nonzero $e \in \mathfrak{m}$ with $\mathfrak{m} e = 0$.

Lean: `GlobalTheory.SiegelArtin.exists_socle`.

*Proof.* The ideal $\mathfrak{m}$ is nilpotent (Atiyah and Macdonald, *Introduction to Commutative Algebra*, Chapter 8). Let $k$ be the least integer with $\mathfrak{m}^k = 0$. Then $k \neq 0$ since $C \neq 0$, and $k \neq 1$ since $\mathfrak{m} \neq 0$. So $k - 1 \geq 1$ and $\mathfrak{m}^{k-1} \neq 0$. Choose a nonzero $e \in \mathfrak{m}^{k-1} \subseteq \mathfrak{m}$. Then $\mathfrak{m} e \subseteq \mathfrak{m}^k = 0$. $\square$

**Theorem 8.5.2 (Classification over Artinian local rings).** Let $C$ be a local Artinian ring with a map $\beta : B_M \to C$. Then $F$ classifies every principal Siegel object over $\operatorname{Spec} C$.

Lean: `GlobalTheory.SiegelArtin.main` (also `GlobalTheory.T.siegel_point_lifts_to_artinian`).

*Proof.* The ring $C$ has finite length $N$ as a module over itself. We use strong induction on $N$. Let $c$ be a principal Siegel object over $C$. If $\mathfrak{m} = 0$, then $C$ is a field and result 1 gives the claim. Otherwise the lemma gives a nonzero $e \in \mathfrak{m}$ with $\mathfrak{m} e = 0$. The exact sequence $0 \to (e) \to C \to C/(e) \to 0$ gives $N = \ell(e) + \ell(C/(e))$, where $\ell$ is the length over $C$, and $\ell(e) > 0$ since $e \neq 0$. The length of $C/(e)$ over $C$ equals its length over itself. So $C/(e)$ is a local Artinian ring of length less than $N$. Let $c_0$ be a Siegel object over $C/(e)$ with a map $c_0 \to c$ over the quotient map. By result 2 it is principal, and by induction $F$ classifies it. The [small extension theorem](/entry/classified-of-small/) shows that $F$ classifies $c$. $\square$

### Complete noetherian local rings

For a ring $R$ with an ideal $I$ and $e \geq 0$ we write $t_e : \operatorname{Spec}(R/I^{e+1}) \to \operatorname{Spec} R$ for the closed immersion. We use the following results.

3. (Uniqueness of classifying maps.) Let $c$ be a Siegel object over $s' : S \to \operatorname{Spec} B_M$, and let $f, f' : S \to X$ with $s f = s f' = s'$, such that there are maps $c \to u$ over $f$ and over $f'$. Then $f = f'$.
4. (Maps from a complete local ring.) Let $R$ be a local ring that is complete for its maximal ideal $\mathfrak{m}$, and let $X$ be a scheme. A compatible system of maps $x_e : \operatorname{Spec}(R/\mathfrak{m}^{e+1}) \to X$ comes from a map $\operatorname{Spec} R \to X$. All the $x_e$ send the one point to the same point of $X$, so they factor through one affine open $\operatorname{Spec} A$, and the compatible ring maps $A \to R/\mathfrak{m}^{e+1}$ give a map $A \to \varprojlim R/\mathfrak{m}^{e+1} = R$.
5. (Rigidity.) Let $c$ be a principal Siegel object and let $\varphi, \varphi'$ be two maps $c' \to c$ over the same $f$. Then $\varphi = \varphi'$ as maps of abelian schemes. This is the rigidity of [level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures) of level $M \geq 3$.
6. (Algebraization of maps.) Let $R$ be noetherian and complete for an ideal $I$, let $c$ and $c'$ be Siegel objects over $\operatorname{Spec} R$ with $c$ principal, and let $c_e$ be Siegel objects over $R/I^{e+1}$ with maps $\varphi_e : c_e \to c$ and $\psi_e : c_e \to c'$ over $t_e$. Suppose that there are maps $\beta_e$ from the abelian scheme of $c_e$ to that of $c_{e+1}$ with $\varphi_{e+1} \beta_e = \varphi_e$ and $\psi_{e+1} \beta_e = \psi_e$. Then there is a map $c \to c'$ over the identity. This is an application of [Grothendieck's existence theorem](/learn/commutative-algebra/#formal-functions-and-grothendiecks-existence-theorem) (EGA III$_1$, §5.4), since $\Delta^* P$ is relatively ample on $c$.

**Lemma 8.5.3 (Separation).** Let $R$ be separated for the $I$-adic topology and let $f, f' : \operatorname{Spec} R \to \operatorname{Spec} A$ with $f t_e = f' t_e$ for every $e$. Then $f = f'$.

Lean: `GlobalTheory.SFamCompl.ext_affine`.

*Proof.* The maps come from ring maps $\alpha, \alpha' : A \to R$. For $a \in A$ the hypothesis gives $\alpha(a) - \alpha'(a) \in I^{e+1}$ for every $e$. Since $\bigcap_e I^{e+1} = 0$, we get $\alpha(a) = \alpha'(a)$. $\square$

**Lemma 8.5.4 (Formal maps algebraize).** Let $R$ be noetherian and complete for an ideal $I$, and let $c$ and $c'$ be principal Siegel objects over $\operatorname{Spec} R$. Suppose that for every $e$ there is a Siegel object $c_e$ over $R/I^{e+1}$ that is a pullback of $c$ and of $c'$ along $t_e$. Then there is a map $c \to c'$ over the identity.

Lean: `GlobalTheory.SFamCompl.alg` (also `GlobalTheory.SFamCompl.tower`, `GlobalTheory.SFamCompl.assemble`).

*Proof.* Let $\varphi_e : c_e \to c$ and $\psi_e : c_e \to c'$ be the given maps over $t_e$. By the cancellation rule there is a map $\beta_e : c_e \to c_{e+1}$ over the closed immersion $\operatorname{Spec}(R/I^{e+1}) \to \operatorname{Spec}(R/I^{e+2})$. Then $\varphi_{e+1} \beta_e$ and $\varphi_e$ are two maps $c_e \to c$ over $t_e$, so they are equal by result 5 since $c$ is principal. In the same way $\psi_{e+1} \beta_e = \psi_e$, since $c'$ is principal. Result 6 gives the map $c \to c'$. $\square$

**Theorem 8.5.5 (Classification over complete noetherian local rings).** Let $R$ be a noetherian local ring that is complete for its maximal ideal $\mathfrak{m}$, with a map $\beta : B_M \to R$. Then $F$ classifies every principal Siegel object over $\operatorname{Spec} R$.

Lean: `GlobalTheory.SFamCompl.classified_of_complete` (also `GlobalTheory.T.siegelFamily_classifies_complete_noetherian_local`).

*Proof.* Let $c$ be principal over $R$. For every $e$ the ring $R/\mathfrak{m}^{e+1}$ is local, and it is Artinian since it is noetherian and its only prime is $\mathfrak{m}/\mathfrak{m}^{e+1}$. Let $c_e$ be a pullback of $c$ along $t_e$. It is principal, so the theorem above gives $x_e : \operatorname{Spec}(R/\mathfrak{m}^{e+1}) \to X$ over $B_M$ with a map $c_e \to u$ over $x_e$. Let $\tau_e$ be the closed immersion of $\operatorname{Spec}(R/\mathfrak{m}^{e+1})$ into $\operatorname{Spec}(R/\mathfrak{m}^{e+2})$. By the cancellation rule there is a map $c_e \to c_{e+1}$ over $\tau_e$, and so a map $c_e \to u$ over $x_{e+1} \tau_e$. Result 3 shows that $x_{e+1} \tau_e = x_e$. Result 4 gives $f : \operatorname{Spec} R \to X$ with $f t_e = x_e$ for every $e$. The maps $s f$ and $\operatorname{Spec} \beta$ agree after $t_e$ for every $e$, and $R$ is separated, so $s f = \operatorname{Spec} \beta$ by the separation lemma. Let $c'$ be a pullback of $u$ along $f$. It is principal, and $c_e$ is a pullback of $c'$ along $t_e$, since $c_e \to u$ over $x_e = f t_e$. The lemma on formal maps gives a map $c \to c'$ over the identity. Its composite with $c' \to u$ is a map $c \to u$ over $f$. $\square$

### Noetherian local rings

We use one more result.

7. (Faithfully flat descent.) Let $R \to R'$ be a [[faithfully flat|C31PYYPRGC]] ring map, $\beta : B_M \to R$, and $c$ a principal Siegel object over $\operatorname{Spec} R$. If $F$ classifies every Siegel object $c'$ over $\operatorname{Spec} R'$ with a map $c' \to c$, then $F$ classifies $c$.

**Theorem 8.5.6 (Classification over noetherian local rings).** Let $R$ be a noetherian local ring with a map $\beta : B_M \to R$. Then $F$ classifies every principal Siegel object over $\operatorname{Spec} R$.

Lean: `GlobalTheory.SiegelFamLocal.exists_point_of_principal` (also `GlobalTheory.T.siegelFamily_classifies_noetherian_local`).

*Proof.* Let $\widehat{R}$ be the $\mathfrak{m}$-adic completion of $R$. It is a noetherian local ring, complete for its maximal ideal, and the map $R \to \widehat{R}$ is flat and local, so faithfully flat (Matsumura, *Commutative Ring Theory*, §8). Let $c'$ be a Siegel object over $\widehat{R}$ with a map $c' \to c$. Then $c'$ is principal by result 2, and the theorem on complete rings shows that $F$ classifies $c'$. Result 7 shows that $F$ classifies $c$. $\square$

In the theorem on complete rings the comparison of $c$ with $f^* u$ happens only through the formal objects $c_e$. The map $f$ is built first, and the isomorphism is algebraized after.

**Remark 8.5.7 (Formalization).** The name `GlobalTheory.T.siegel_point_lifts_to_artinian` claims less than its statement, which classifies every principal Siegel object over a local Artinian ring. The induction is on the length of $C$ as a module over itself, and the length of $C/(e)$ over $C$ is compared with its length over itself: [SiegelPointLiftsToArtinian.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelPointLiftsToArtinian.lean#L47). The results 4 and 6 enter as second names for results proved elsewhere: [SiegelFamilyClassifiesCompleteNoetherianLocal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesCompleteNoetherianLocal.lean#L19) and [SiegelFamilyClassifiesCompleteNoetherianLocal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesCompleteNoetherianLocal.lean#L77). Result 6 needs only that $c$ is principal and that $R$ is noetherian and complete for $I$; the lemma on formal maps does not use that $R$ is local. Result 3 does not ask that $c$ is principal. The file repeats two small helpers on $\operatorname{Spec}$ of compositions and of identities that the file on noetherian rings also defines: [SiegelFamilyClassifiesCompleteNoetherianLocal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesCompleteNoetherianLocal.lean#L116). The descent to noetherian local rings is in [SiegelFamilyClassifiesNoetherianLocal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesNoetherianLocal.lean#L16). We read the statements of results 1 to 7, not their proofs.
